"""
A simple example of using LangChain and LangGraph.
"""
from langchain_core.messages import HumanMessage
from langgraph_task import create_agent_graph

def main():
    """Run the example."""
    # Create the graph
    graph = create_agent_graph()
    
    # Create initial state
    state = {
        "messages": [HumanMessage(content="Hello from example!")],
        "next_step": "process"
    }
    
    # Run the graph
    result = graph.invoke(state)
    print("\nFinal state:", result)

if __name__ == "__main__":
    main()