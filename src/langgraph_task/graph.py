"""
Core functionality for LangGraph task processing.
"""
from typing import Dict, TypedDict, Annotated, Sequence
from operator import itemgetter

from langchain_core.messages import HumanMessage, BaseMessage
from langgraph.graph import Graph, StateGraph
from langchain_core.runnables import RunnableConfig

class AgentState(TypedDict):
    """State for the agent."""
    messages: Sequence[BaseMessage]
    next_step: str | None

def process_message(state: AgentState) -> AgentState:
    """Process a message in the conversation."""
    # Validate state
    if not isinstance(state, dict):
        raise ValueError("State must be a dictionary")
    
    if "messages" not in state:
        raise KeyError("State must contain 'messages' key")
        
    if "next_step" not in state:
        raise KeyError("State must contain 'next_step' key")
        
    if not state["messages"]:
        raise ValueError("Messages sequence cannot be empty")
    
    # In a real application, you would process the message here
    print("Processing message:", state["messages"][-1].content)
    return {"messages": state["messages"], "next_step": None}

def create_agent_graph() -> Graph:
    """Create a simple agent graph."""
    # Create an empty graph
    workflow = StateGraph(AgentState)
    
    # Define the nodes
    workflow.add_node("process", process_message)
    
    # Define the edges
    workflow.set_entry_point("process")
    
    # Compile the graph
    return workflow.compile() 