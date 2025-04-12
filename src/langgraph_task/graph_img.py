      # 生成流程图
from langchain_core.runnables.graph import MermaidDrawMethod 
from langgraph.graph import Graph
from typing import Optional

# 生成流程图并保存为PNG文件 
def graph_img(graph: Graph, output_file_path: str, draw_method: Optional[MermaidDrawMethod] = None) -> None:
    """
    生成流程图并保存为PNG文件
    
    Args:
        graph (Graph): LangGraph图对象
        output_file_path (str): 输出PNG文件路径
        draw_method (Optional[MermaidDrawMethod]): 绘图方法,默认使用API方式
    
    Returns:
        None
    
    Raises:
        ValueError: 如果graph为None或output_file_path为空
    """
    if not graph:
        raise ValueError("Graph object cannot be None")
    if not output_file_path:
        raise ValueError("Output file path cannot be empty")
        
    draw_method = draw_method or MermaidDrawMethod.API
    
    try:
        # 生成流程图
        graph.get_graph().draw_mermaid_png(
            draw_method=draw_method,
            output_file_path=output_file_path
        )
    except Exception as e:
        raise RuntimeError(f"Failed to generate graph image: {str(e)}")
