"""
Command line interface for langgraph-task.
"""
from langchain_core.messages import HumanMessage

from .graph import create_agent_graph

def main():
    """Main entry point for the application."""
    # Create the graph
    graph = create_agent_graph()
    
    # Create initial state
    state = {
        "messages": [HumanMessage(content="Hello from CLI!")],
        "next_step": "process"
    }
    
    # Run the graph
    result = graph.invoke(state)
    print("\nFinal state:", result)
    return 0

if __name__ == "__main__":
    main() 