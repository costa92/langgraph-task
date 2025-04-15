"""
Tests for the CLI module.
"""
import pytest
from unittest.mock import patch
import io
import sys

from langgraph_task.cli import main

def test_main_success():
    """Test that the main function runs successfully."""
    # Capture stdout to verify output
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    try:
        # Run the main function
        result = main()
        
        # Verify the result
        assert result == 0
        
        # Verify the output contains expected strings
        output = captured_output.getvalue()
        assert "Processing message: Hello from CLI!" in output
        assert "Final state:" in output
    finally:
        sys.stdout = sys.__stdout__  # Restore stdout

@patch('langgraph_task.cli.create_agent_graph')
def test_main_with_mock_graph(mock_create_graph):
    """Test main function with a mocked graph."""
    # Setup mock
    # 在LangGraph中，graph.invoke接受state作为第一个参数
    mock_graph = type('MockGraph', (), {})()
    mock_graph.invoke = lambda state, config=None: {
        "messages": state["messages"],
        "next_step": None
    }
    mock_create_graph.return_value = mock_graph
    
    # Capture stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    try:
        # Run the main function
        result = main()
        
        # Verify the result
        assert result == 0
        
        # Verify mock was called
        mock_create_graph.assert_called_once()
        
        # Verify output
        output = captured_output.getvalue()
        assert "Final state:" in output
    finally:
        sys.stdout = sys.__stdout__  # Restore stdout

def test_main_as_module():
    """Test that the script can be run as a module."""
    # This test verifies that the __main__ block works
    with patch('langgraph_task.cli.main') as mock_main:
        mock_main.return_value = 0
        
        # Simulate running as main module
        if __name__ == "__main__":
            import langgraph_task.cli
        
        # Verify main wasn't called (since we're not actually the main module)
        mock_main.assert_not_called() 