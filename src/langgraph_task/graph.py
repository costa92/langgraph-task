"""
Core functionality for LangGraph task processing.
"""
from typing import Dict, TypedDict, Annotated, Sequence
from operator import itemgetter

from langchain_core.messages import HumanMessage, BaseMessage
from langgraph.graph import Graph, StateGraph, END
from langchain_core.runnables import RunnableConfig
from langgraph_task.llm import LLM
from langgraph_task.llm.call import call_model

class AgentState(TypedDict):
    """State for the agent."""
    messages: Sequence[BaseMessage]
    next_step: str | None

def process_message(state: AgentState) -> AgentState:
    """Process messages in conversation."""
    if not isinstance(state, dict):
        raise ValueError("State must be a dictionary")
    
    if "messages" not in state or "next_step" not in state:
        raise KeyError("State must contain 'messages' and 'next_step' keys")
        
    if not state["messages"]:
        raise ValueError("Message sequence cannot be empty")
    
    print(f"Processing message: {state['messages'][-1].content}")
    return {"messages": state["messages"], "next_step": None}

def create_agent_graph() -> Graph:
    """Create a simple agent graph."""
    workflow = StateGraph(AgentState)
    
    workflow.add_node("process", process_message)
    workflow.set_entry_point("process")
    
    return workflow.compile()

def task_decomposition(state: AgentState) -> AgentState:
    """Decompose tasks into subtasks."""
    return {"messages": state["messages"], "next_step": None}

def call_model(state: AgentState) -> AgentState:
    """Call the model."""
    return {"messages": state["messages"], "next_step": None}

# 任务分解
def create_task_decomposition_graph() -> Graph:
    """Create a task decomposition graph."""
    workflow = StateGraph(AgentState)
    llm = LLM(model_name="deepseek-chat")

    def llm_node(state: AgentState) -> AgentState:
        """LLM processing node."""
        response = call_model(state["messages"])
        messages = list(state["messages"])
        messages.append(response)
        return {"messages": messages, "next_step": None}

    workflow.add_node("task_decomposition", task_decomposition)
    workflow.add_node("llm", llm_node)

    workflow.set_entry_point("task_decomposition")
    workflow.add_edge("task_decomposition", "llm")
    workflow.add_edge("llm", "task_decomposition")
    workflow.add_edge("task_decomposition", END)
    
    return workflow.compile()

def create_task_execution_graph() -> Graph:
    """Create a task execution graph."""