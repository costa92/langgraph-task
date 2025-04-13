#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from langchain_core.tools import BaseTool
from langgraph_task.tools.tools_list import tools_list,search_web

@pytest.mark.performance
def test_tools_list():
    """测试工具列表的基本属性和功能"""
    # 测试工具列表不为空
    assert len(tools_list) > 0, "工具列表不能为空"
    
    # 测试所有工具都是BaseTool的实例
    for tool in tools_list:
        assert isinstance(tool, BaseTool), f"{tool} 不是BaseTool的实例"
        
    # 测试工具都有必要的属性
    for tool in tools_list:
        assert hasattr(tool, "name"), f"{tool} 缺少name属性"
        assert hasattr(tool, "description"), f"{tool} 缺少description属性"
        assert callable(tool.run), f"{tool} 的run方法不可调用"

@pytest.mark.performance
def test_search_web():
    """测试搜索引擎工具"""
    result = search_web.invoke("Python 教程")
    print(result)
