#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Optional, Union, Any
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_deepseek import ChatDeepSeek
from langchain.chat_models.base import BaseChatModel


class LLM:
    """A wrapper class for multiple LLM providers with default parameters."""
    
    llm: Union[ChatOpenAI, ChatGoogleGenerativeAI, ChatDeepSeek, BaseChatModel]
    
    def __init__(
        self,
        model_name: str = "gpt-4-turbo-preview",
        temperature: float = 0.0,
        max_tokens: Optional[int] = 1000,
        top_p: float = 1.0,
        frequency_penalty: float = 0.0,
        presence_penalty: float = 0.0,
        custom_llm: Optional[BaseChatModel] = None,
        **kwargs: Any
    ) -> None:
        """Initialize the LLM wrapper.
        
        Args:
            model_name: The name of the model to use (supports OpenAI, Google and DeepSeek models)
            temperature: Controls randomness in responses
            max_tokens: Maximum number of tokens to generate
            top_p: Nucleus sampling parameter
            frequency_penalty: Penalizes frequent tokens (OpenAI only)
            presence_penalty: Penalizes repeated tokens (OpenAI only)
            custom_llm: Custom LLM instance that inherits from BaseChatModel
            **kwargs: Additional keyword arguments passed to the LLM constructor
        """
        if custom_llm is not None:
            if not isinstance(custom_llm, BaseChatModel):
                raise ValueError("custom_llm must inherit from BaseChatModel")
            self.llm = custom_llm
        elif model_name.startswith("gpt"):
            self.llm = ChatOpenAI(
                model=model_name,
                temperature=temperature,
                max_tokens=max_tokens,
                top_p=top_p,
                frequency_penalty=frequency_penalty,
                presence_penalty=presence_penalty,
                **kwargs
            )
        elif model_name.startswith("gemini"):
            self.llm = ChatGoogleGenerativeAI(
                model=model_name,
                temperature=temperature,
                max_output_tokens=max_tokens,
                top_p=top_p,
                **kwargs
            )
        elif model_name.startswith("deepseek"):
            self.llm = ChatDeepSeek(
                model=model_name,
                temperature=temperature,
                max_tokens=max_tokens,
                top_p=top_p,
                **kwargs
            )
        else:
            raise ValueError(f"Unsupported model: {model_name}")
