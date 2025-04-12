# LangGraph Task 测试运行文档

## 目录

- [1. 基础测试命令](#1-基础测试命令)
- [2. 单个测试方法运行命令](#2-单个测试方法运行命令)
- [3. 特定标记测试](#3-特定标记测试)
- [4. 调试相关命令](#4-调试相关命令)
- [5. 生成测试报告](#5-生成测试报告)
- [6. 常用选项说明](#6-常用选项说明)
- [7. 环境要求](#7-环境要求)
- [8. 注意事项](#8-注意事项)
- [9. 配置文件](#9-配置文件)

## 1. 基础测试命令

### 运行所有测试

```bash
pytest tests/test_graph.py -v
```

### 运行带覆盖率报告的测试

```bash
pytest tests/test_graph.py -v --cov=langgraph_task --cov-report=term-missing
```

## 2. 单个测试方法运行命令

### 2.1 AgentState 类型测试

```bash
pytest tests/test_graph.py::test_agent_state_type -v
```

**测试说明**：验证 AgentState 类型是否可以正确实例化和使用。

### 2.2 消息处理测试

```bash
pytest tests/test_graph.py::test_process_message -v
```

**测试说明**：验证 process_message 函数的基本功能。

### 2.3 代理图创建测试

```bash
pytest tests/test_graph.py::test_create_agent_graph -v
```

**测试说明**：验证代理图的创建和基本执行功能。

### 2.4 不同消息内容测试
```bash
pytest tests/test_graph.py::test_graph_with_different_messages -v
```
**测试说明**：使用参数化测试验证不同消息内容的处理。

### 2.5 无效状态测试
```bash
pytest tests/test_graph.py::test_invalid_state -v
```
**测试说明**：验证对无效输入状态的错误处理。

### 2.6 系统消息测试
```bash
pytest tests/test_graph.py::test_process_message_with_system_message -v
```
**测试说明**：验证包含系统消息的消息链处理。

### 2.7 性能测试
```bash
pytest tests/test_graph.py::test_large_message_processing -v -m performance
```
**测试说明**：验证处理大量消息时的性能表现。

## 3. 特定标记测试

### 3.1 只运行性能测试
```bash
pytest tests/test_graph.py -v -m "performance"
```

### 3.2 运行非性能测试
```bash
pytest tests/test_graph.py -v -m "not performance"
```

## 4. 调试相关命令

### 4.1 显示详细输出
```bash
pytest tests/test_graph.py -v -s
```

### 4.2 失败时显示完整回溯
```bash
pytest tests/test_graph.py -v --tb=long
```

### 4.3 停在第一个失败的测试
```bash
pytest tests/test_graph.py -v -x
```

## 5. 生成测试报告

### 5.1 生成 HTML 覆盖率报告
```bash
pytest tests/test_graph.py --cov=langgraph_task --cov-report=html
```

### 5.2 生成 XML 覆盖率报告

```bash
pytest tests/test_graph.py --cov=langgraph_task --cov-report=xml
```

## 6. 常用选项说明

- `-v`: 显示详细输出
- `-s`: 显示打印输出
- `-x`: 首次失败时停止
- `-m`: 运行带特定标记的测试
- `--tb=short`: 简短的回溯信息
- `--maxfail=2`: 失败 2 次后停止
- `-k "test_name"`: 按测试名称模式运行

## 7. 环境要求

- Python >= 3.12
- pytest >= 6.0
- pytest-cov >= 2.0
- langchain >= 0.1.0
- langgraph >= 0.0.17
- langchain-core >= 0.1.0
- langchain-community >= 0.3.21

## 8. 注意事项

1. 运行性能测试前确保系统资源充足
2. 覆盖率报告会显示未测试的代码行
3. 使用 `-s` 选项可以看到测试中的打印输出
4. 测试失败时使用 `--tb=long` 查看详细错误信息

## 9. 配置文件

测试配置位于 `pyproject.toml` 文件中，包含了：

- 测试路径配置
- 测试文件模式
- 测试函数命名规则
- 测试标记定义
- 覆盖率报告配置 
