#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Any, List, Optional, Union
from langchain_core.messages import BaseMessage
from langchain_core.language_models.chat_models import BaseChatModel
from .llm import LLM

def call_model(
    messages: List[BaseMessage],
    model: Optional[Union[BaseChatModel, LLM]] = None,
    **kwargs: Any
) -> BaseMessage:
    """Call the language model with the given messages.

    Args:
        messages: List of messages to send to the model
        model: Optional model instance to use. If not provided, creates default LLM
        **kwargs: Additional arguments passed to the model invoke

    Returns:
        The model's response message

    Raises:
        ValueError: If messages list is empty
    """
    if not messages:
        raise ValueError("Messages list cannot be empty")

    # Use provided model or create default LLM
    llm = model.llm if isinstance(model, LLM) else model or LLM().llm

    # Call the model and return response
    return llm.invoke(messages, **kwargs)
