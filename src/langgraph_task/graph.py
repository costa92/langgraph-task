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
    """处理会话中的消息。"""
    # 验证状态对象
    if not isinstance(state, dict):
        raise ValueError("状态必须是字典类型")
    
    # 验证状态字典中是否包含messages键
    if "messages" not in state:
        raise KeyError("状态字典必须包含'messages'键")
        
    # 验证状态字典中是否包含next_step键
    if "next_step" not in state:
        raise KeyError("状态字典必须包含'next_step'键")
        
    # 验证消息序列不能为空
    if not state["messages"]:
        raise ValueError("消息序列不能为空")
    
    # In a real application, you would process the message here
    print("Processing message:", state["messages"][-1].content)
    return {"messages": state["messages"], "next_step": None}

# 创建一个简单的代理图
def create_agent_graph() -> Graph:
    """创建一个简单的代理图。"""
    # 创建一个空的图
    workflow = StateGraph(AgentState)
    
    # 定义节点
    workflow.add_node("process", process_message)
    
    # 定义边缘
    workflow.set_entry_point("process")
    
    # 编译图
    return workflow.compile()


def task_decomposition(state: AgentState) -> AgentState:
    """任务分解。"""
    return {"messages": state["messages"], "next_step": None} 

# 创建一个简单的任务分解图  
def create_task_decomposition_graph() -> Graph:
    """创建一个简单的任务分解图。"""
    # 创建一个空的图
    workflow = StateGraph(AgentState)
    
    # 定义节点
    workflow.add_node("task_decomposition", task_decomposition)

    # 定义边缘
    workflow.set_entry_point("task_decomposition")
    
    # 编译图    
    return workflow.compile()


# 创建一个简单的任务执行图
def create_task_execution_graph() -> Graph:
    """创建一个简单的任务执行图。"""