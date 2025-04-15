#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from unittest.mock import patch, MagicMock
from langgraph_task.llm import LLM
from langchain_core.messages import HumanMessage, AIMessage

@pytest.mark.performance
def test_llm_performance():
    """Test the performance of the LLM."""
    # Create mock response
    mock_response = AIMessage(content="Test response")
    mock_llm = MagicMock()
    mock_llm.invoke.return_value = mock_response
    
    # Patch ChatOpenAI
    with patch('langgraph_task.llm.llm.ChatOpenAI') as mock_chat:
        mock_chat.return_value = mock_llm
        
        # Create LLM instance and test
        llm = LLM(model_name="gpt-3.5-turbo").llm
        messages = [HumanMessage(content="Hello, world!")]
        result = llm.invoke(messages)
        
        # Verify result
        assert result == mock_response
        mock_llm.invoke.assert_called_once_with(messages)

    
