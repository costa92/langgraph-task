#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pytest
from langgraph_task.llm import LLM
from langchain_core.messages import HumanMessage

@pytest.mark.performance
def test_llm_performance():
    """Test the performance of the LLM."""
    llm = LLM(model_name="deepseek-chat").llm
    result = llm.invoke("Hello, world!")
    print(result)

    
