# LangGraph Task API 文档

## 1. 核心 API

### 1.1 AgentState
```python
class AgentState(TypedDict):
    """任务代理状态类型定义。"""
    messages: Sequence[BaseMessage]  # 消息序列
    next_step: str | None           # 下一步操作
```

**描述**：
- `messages`：存储消息历史的序列
- `next_step`：指示下一步操作的标识符

**示例**：
```python
state = {
    "messages": [HumanMessage(content="Hello")],
    "next_step": "process"
}
```

### 1.2 process_message
```python
def process_message(state: AgentState) -> AgentState:
    """处理消息并更新状态。"""
```

**参数**：
- `state`：当前任务状态

**返回值**：
- 更新后的任务状态

**异常**：
- `ValueError`：状态对象类型错误
- `KeyError`：状态字典缺少必要键
- `ValueError`：消息序列为空

**示例**：
```python
result = process_message({
    "messages": [HumanMessage(content="Process this message")],
    "next_step": "process"
})
```

### 1.3 create_agent_graph
```python
def create_agent_graph() -> Graph:
    """创建任务处理图。"""
```

**返回值**：
- 编译后的任务图

**示例**：
```python
graph = create_agent_graph()
```

## 2. 使用指南

### 2.1 基本用法

1. **创建状态**
```python
from langchain_core.messages import HumanMessage
from langgraph_task import AgentState

state = AgentState(
    messages=[HumanMessage(content="Initial message")],
    next_step="process"
)
```

2. **处理消息**
```python
from langgraph_task import process_message

updated_state = process_message(state)
```

3. **创建和使用图**
```python
from langgraph_task import create_agent_graph

graph = create_agent_graph()
result = graph.invoke({
    "messages": [HumanMessage(content="Test message")],
    "next_step": "process"
})
```

### 2.2 高级用法

#### 自定义节点
```python
from langgraph.graph import StateGraph

def custom_node(state: AgentState) -> AgentState:
    # 自定义节点逻辑
    return state

workflow = StateGraph(AgentState)
workflow.add_node("custom", custom_node)
workflow.set_entry_point("custom")
graph = workflow.compile()
```

#### 异步操作
```python
async def async_process(state: AgentState) -> AgentState:
    # 异步处理逻辑
    return state

# 使用异步图
async_graph = workflow.compile()
result = await async_graph.ainvoke(initial_state)
```

## 3. 工具函数

### 3.1 状态验证
```python
def validate_state(state: AgentState) -> bool:
    """验证状态对象是否有效。"""
    if not isinstance(state, dict):
        return False
    if "messages" not in state or "next_step" not in state:
        return False
    if not state["messages"]:
        return False
    return True
```

### 3.2 消息处理
```python
def create_message(content: str) -> HumanMessage:
    """创建新的消息对象。"""
    return HumanMessage(content=content)
```

## 4. 配置选项

### 4.1 图配置
```python
from langchain_core.runnables import RunnableConfig

config = RunnableConfig(
    max_iterations=10,
    recursion_limit=100
)
```

### 4.2 状态配置
```python
state_config = {
    "max_messages": 1000,
    "timeout": 30
}
```

## 5. 错误处理

### 5.1 常见错误
1. **状态验证错误**
```python
try:
    result = process_message(invalid_state)
except ValueError as e:
    print(f"状态验证失败: {e}")
except KeyError as e:
    print(f"缺少必要的状态键: {e}")
```

2. **图执行错误**
```python
try:
    result = graph.invoke(state)
except Exception as e:
    print(f"图执行失败: {e}")
```

## 6. 最佳实践

### 6.1 状态管理
- 保持状态对象简洁
- 及时清理不需要的消息
- 使用类型注解确保类型安全

### 6.2 图设计
- 保持图结构清晰
- 避免复杂的循环依赖
- 适当使用边缘条件

### 6.3 错误处理
- 实现完整的错误处理逻辑
- 提供有意义的错误信息
- 记录关键操作日志

## 7. 性能优化

### 7.1 消息处理优化
- 限制消息历史大小
- 使用异步处理大量消息
- 实现消息批处理

### 7.2 图执行优化
- 减少不必要的节点
- 优化节点执行顺序
- 使用缓存机制

## 8. 安全考虑

### 8.1 输入验证
- 验证所有外部输入
- 清理消息内容
- 限制消息大小

### 8.2 资源控制
- 限制最大执行时间
- 控制内存使用
- 实现限流机制 