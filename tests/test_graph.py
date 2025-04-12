"""
Tests for the graph module.
"""
import pytest
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph_task.graph import (
    AgentState,
    process_message,
    create_agent_graph,
)
from langgraph_task.graph_img import graph_img


def test_agent_state_type():
    """Test that AgentState type can be instantiated correctly."""
    # Create a valid state
    state: AgentState = {
        "messages": [HumanMessage(content="test")],
        "next_step": "process"
    }
    
    assert isinstance(state, dict)
    assert "messages" in state
    assert "next_step" in state
    assert isinstance(state["messages"], (list, tuple))
    assert isinstance(state["messages"][0], HumanMessage)
    assert isinstance(state["next_step"], (str, type(None)))

def test_process_message():
    """Test the process_message function."""
    # Create test input
    test_message = "Hello, test!"
    state: AgentState = {
        "messages": [HumanMessage(content=test_message)],
        "next_step": "process"
    }
    
    # Process the message
    result = process_message(state)
    
    # Verify the result
    assert isinstance(result, dict)
    assert "messages" in result
    assert "next_step" in result
    assert result["messages"] == state["messages"]
    assert result["next_step"] is None

def test_create_agent_graph():
    """Test the create_agent_graph function."""
    # Create the graph
    graph = create_agent_graph()
    
    # Test with a simple message
    state = {
        "messages": [HumanMessage(content="Test message")],
        "next_step": "process"
    }
    
    # Run the graph
    result = graph.invoke(state)
    
    graph_img(graph, "test_agent_graph.png")

    # Verify the result
    assert isinstance(result, dict)
    assert "messages" in result
    assert "next_step" in result
    assert len(result["messages"]) == 1
    assert result["messages"][0].content == "Test message"
    assert result["next_step"] is None


@pytest.mark.parametrize("message_content,expected_next_step", [
    ("Hello", None),
    ("Test", None),
    ("Complex message with spaces", None),
])
def test_graph_with_different_messages(message_content, expected_next_step):
    """Test the graph with different message contents."""
    graph = create_agent_graph()
    
    state = {
        "messages": [HumanMessage(content=message_content)],
        "next_step": "process"
    }
    
    result = graph.invoke(state)
    
    assert result["next_step"] == expected_next_step
    assert result["messages"][0].content == message_content

def test_invalid_state():
    """Test that the process_message function handles invalid state."""
    with pytest.raises(ValueError):
        process_message("not a dict")  # Not a dictionary
    
    with pytest.raises(KeyError):
        process_message({})  # Empty state
    
    with pytest.raises(KeyError):
        process_message({"messages": []})  # Missing next_step
        
    with pytest.raises(KeyError):
        process_message({"next_step": "process"})  # Missing messages
        
    with pytest.raises(ValueError):
        process_message({"messages": [], "next_step": "process"})  # Empty messages

def test_process_message_with_system_message():
    """Test processing a message with a system message in the chain."""
    state: AgentState = {
        "messages": [
            SystemMessage(content="System instruction"),
            HumanMessage(content="User message")
        ],
        "next_step": "process"
    }
    
    result = process_message(state)
    
    assert isinstance(result, dict)
    assert len(result["messages"]) == 2
    assert isinstance(result["messages"][0], SystemMessage)
    assert isinstance(result["messages"][1], HumanMessage)
    assert result["messages"][1].content == "User message"

@pytest.mark.performance
def test_large_message_processing():
    """Test processing of large messages for performance."""
    # Create a large message
    large_message = "test " * 1000
    state: AgentState = {
        "messages": [HumanMessage(content=large_message)],
        "next_step": "process"
    }
    
    # Process the message and measure time
    import time
    start_time = time.time()
    result = process_message(state)
    end_time = time.time()
    
    # Verify the result
    assert isinstance(result, dict)
    assert "messages" in result
    assert "next_step" in result
    assert result["messages"] == state["messages"]
    assert result["next_step"] is None
    
    # Check processing time (adjust threshold as needed)
    processing_time = end_time - start_time
    assert processing_time < 1.0, f"Processing took too long: {processing_time} seconds" 