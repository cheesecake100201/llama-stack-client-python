# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types import (
    InferenceCompletionResponse,
    InferenceChatCompletionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInference:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_chat_completion_overload_1(self, client: LlamaStackClient) -> None:
        inference = client.inference.chat_completion(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
            ],
            model="model",
        )
        assert_matches_type(InferenceChatCompletionResponse, inference, path=["response"])

    @parametrize
    def test_method_chat_completion_with_all_params_overload_1(self, client: LlamaStackClient) -> None:
        inference = client.inference.chat_completion(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                    "context": "string",
                },
                {
                    "content": "string",
                    "role": "user",
                    "context": "string",
                },
                {
                    "content": "string",
                    "role": "user",
                    "context": "string",
                },
            ],
            model="model",
            logprobs={"top_k": 0},
            sampling_params={
                "strategy": "greedy",
                "max_tokens": 0,
                "repetition_penalty": 0,
                "temperature": 0,
                "top_k": 0,
                "top_p": 0,
            },
            stream=False,
            tool_choice="auto",
            tool_prompt_format="json",
            tools=[
                {
                    "tool_name": "brave_search",
                    "description": "description",
                    "parameters": {
                        "foo": {
                            "param_type": "param_type",
                            "default": True,
                            "description": "description",
                            "required": True,
                        }
                    },
                },
                {
                    "tool_name": "brave_search",
                    "description": "description",
                    "parameters": {
                        "foo": {
                            "param_type": "param_type",
                            "default": True,
                            "description": "description",
                            "required": True,
                        }
                    },
                },
                {
                    "tool_name": "brave_search",
                    "description": "description",
                    "parameters": {
                        "foo": {
                            "param_type": "param_type",
                            "default": True,
                            "description": "description",
                            "required": True,
                        }
                    },
                },
            ],
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(InferenceChatCompletionResponse, inference, path=["response"])

    @parametrize
    def test_raw_response_chat_completion_overload_1(self, client: LlamaStackClient) -> None:
        response = client.inference.with_raw_response.chat_completion(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
            ],
            model="model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inference = response.parse()
        assert_matches_type(InferenceChatCompletionResponse, inference, path=["response"])

    @parametrize
    def test_streaming_response_chat_completion_overload_1(self, client: LlamaStackClient) -> None:
        with client.inference.with_streaming_response.chat_completion(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
            ],
            model="model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inference = response.parse()
            assert_matches_type(InferenceChatCompletionResponse, inference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_chat_completion_overload_2(self, client: LlamaStackClient) -> None:
        inference_stream = client.inference.chat_completion(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
            ],
            model="model",
            stream=True,
        )
        inference_stream.response.close()

    @parametrize
    def test_method_chat_completion_with_all_params_overload_2(self, client: LlamaStackClient) -> None:
        inference_stream = client.inference.chat_completion(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                    "context": "string",
                },
                {
                    "content": "string",
                    "role": "user",
                    "context": "string",
                },
                {
                    "content": "string",
                    "role": "user",
                    "context": "string",
                },
            ],
            model="model",
            stream=True,
            logprobs={"top_k": 0},
            sampling_params={
                "strategy": "greedy",
                "max_tokens": 0,
                "repetition_penalty": 0,
                "temperature": 0,
                "top_k": 0,
                "top_p": 0,
            },
            tool_choice="auto",
            tool_prompt_format="json",
            tools=[
                {
                    "tool_name": "brave_search",
                    "description": "description",
                    "parameters": {
                        "foo": {
                            "param_type": "param_type",
                            "default": True,
                            "description": "description",
                            "required": True,
                        }
                    },
                },
                {
                    "tool_name": "brave_search",
                    "description": "description",
                    "parameters": {
                        "foo": {
                            "param_type": "param_type",
                            "default": True,
                            "description": "description",
                            "required": True,
                        }
                    },
                },
                {
                    "tool_name": "brave_search",
                    "description": "description",
                    "parameters": {
                        "foo": {
                            "param_type": "param_type",
                            "default": True,
                            "description": "description",
                            "required": True,
                        }
                    },
                },
            ],
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        inference_stream.response.close()

    @parametrize
    def test_raw_response_chat_completion_overload_2(self, client: LlamaStackClient) -> None:
        response = client.inference.with_raw_response.chat_completion(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
            ],
            model="model",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @parametrize
    def test_streaming_response_chat_completion_overload_2(self, client: LlamaStackClient) -> None:
        with client.inference.with_streaming_response.chat_completion(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
            ],
            model="model",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_completion(self, client: LlamaStackClient) -> None:
        inference = client.inference.completion(
            content="string",
            model="model",
        )
        assert_matches_type(InferenceCompletionResponse, inference, path=["response"])

    @parametrize
    def test_method_completion_with_all_params(self, client: LlamaStackClient) -> None:
        inference = client.inference.completion(
            content="string",
            model="model",
            logprobs={"top_k": 0},
            sampling_params={
                "strategy": "greedy",
                "max_tokens": 0,
                "repetition_penalty": 0,
                "temperature": 0,
                "top_k": 0,
                "top_p": 0,
            },
            stream=True,
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(InferenceCompletionResponse, inference, path=["response"])

    @parametrize
    def test_raw_response_completion(self, client: LlamaStackClient) -> None:
        response = client.inference.with_raw_response.completion(
            content="string",
            model="model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inference = response.parse()
        assert_matches_type(InferenceCompletionResponse, inference, path=["response"])

    @parametrize
    def test_streaming_response_completion(self, client: LlamaStackClient) -> None:
        with client.inference.with_streaming_response.completion(
            content="string",
            model="model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inference = response.parse()
            assert_matches_type(InferenceCompletionResponse, inference, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInference:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_chat_completion_overload_1(self, async_client: AsyncLlamaStackClient) -> None:
        inference = await async_client.inference.chat_completion(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
            ],
            model="model",
        )
        assert_matches_type(InferenceChatCompletionResponse, inference, path=["response"])

    @parametrize
    async def test_method_chat_completion_with_all_params_overload_1(self, async_client: AsyncLlamaStackClient) -> None:
        inference = await async_client.inference.chat_completion(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                    "context": "string",
                },
                {
                    "content": "string",
                    "role": "user",
                    "context": "string",
                },
                {
                    "content": "string",
                    "role": "user",
                    "context": "string",
                },
            ],
            model="model",
            logprobs={"top_k": 0},
            sampling_params={
                "strategy": "greedy",
                "max_tokens": 0,
                "repetition_penalty": 0,
                "temperature": 0,
                "top_k": 0,
                "top_p": 0,
            },
            stream=False,
            tool_choice="auto",
            tool_prompt_format="json",
            tools=[
                {
                    "tool_name": "brave_search",
                    "description": "description",
                    "parameters": {
                        "foo": {
                            "param_type": "param_type",
                            "default": True,
                            "description": "description",
                            "required": True,
                        }
                    },
                },
                {
                    "tool_name": "brave_search",
                    "description": "description",
                    "parameters": {
                        "foo": {
                            "param_type": "param_type",
                            "default": True,
                            "description": "description",
                            "required": True,
                        }
                    },
                },
                {
                    "tool_name": "brave_search",
                    "description": "description",
                    "parameters": {
                        "foo": {
                            "param_type": "param_type",
                            "default": True,
                            "description": "description",
                            "required": True,
                        }
                    },
                },
            ],
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(InferenceChatCompletionResponse, inference, path=["response"])

    @parametrize
    async def test_raw_response_chat_completion_overload_1(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.inference.with_raw_response.chat_completion(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
            ],
            model="model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inference = await response.parse()
        assert_matches_type(InferenceChatCompletionResponse, inference, path=["response"])

    @parametrize
    async def test_streaming_response_chat_completion_overload_1(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.inference.with_streaming_response.chat_completion(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
            ],
            model="model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inference = await response.parse()
            assert_matches_type(InferenceChatCompletionResponse, inference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_chat_completion_overload_2(self, async_client: AsyncLlamaStackClient) -> None:
        inference_stream = await async_client.inference.chat_completion(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
            ],
            model="model",
            stream=True,
        )
        await inference_stream.response.aclose()

    @parametrize
    async def test_method_chat_completion_with_all_params_overload_2(self, async_client: AsyncLlamaStackClient) -> None:
        inference_stream = await async_client.inference.chat_completion(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                    "context": "string",
                },
                {
                    "content": "string",
                    "role": "user",
                    "context": "string",
                },
                {
                    "content": "string",
                    "role": "user",
                    "context": "string",
                },
            ],
            model="model",
            stream=True,
            logprobs={"top_k": 0},
            sampling_params={
                "strategy": "greedy",
                "max_tokens": 0,
                "repetition_penalty": 0,
                "temperature": 0,
                "top_k": 0,
                "top_p": 0,
            },
            tool_choice="auto",
            tool_prompt_format="json",
            tools=[
                {
                    "tool_name": "brave_search",
                    "description": "description",
                    "parameters": {
                        "foo": {
                            "param_type": "param_type",
                            "default": True,
                            "description": "description",
                            "required": True,
                        }
                    },
                },
                {
                    "tool_name": "brave_search",
                    "description": "description",
                    "parameters": {
                        "foo": {
                            "param_type": "param_type",
                            "default": True,
                            "description": "description",
                            "required": True,
                        }
                    },
                },
                {
                    "tool_name": "brave_search",
                    "description": "description",
                    "parameters": {
                        "foo": {
                            "param_type": "param_type",
                            "default": True,
                            "description": "description",
                            "required": True,
                        }
                    },
                },
            ],
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        await inference_stream.response.aclose()

    @parametrize
    async def test_raw_response_chat_completion_overload_2(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.inference.with_raw_response.chat_completion(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
            ],
            model="model",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @parametrize
    async def test_streaming_response_chat_completion_overload_2(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.inference.with_streaming_response.chat_completion(
            messages=[
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
            ],
            model="model",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_completion(self, async_client: AsyncLlamaStackClient) -> None:
        inference = await async_client.inference.completion(
            content="string",
            model="model",
        )
        assert_matches_type(InferenceCompletionResponse, inference, path=["response"])

    @parametrize
    async def test_method_completion_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        inference = await async_client.inference.completion(
            content="string",
            model="model",
            logprobs={"top_k": 0},
            sampling_params={
                "strategy": "greedy",
                "max_tokens": 0,
                "repetition_penalty": 0,
                "temperature": 0,
                "top_k": 0,
                "top_p": 0,
            },
            stream=True,
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(InferenceCompletionResponse, inference, path=["response"])

    @parametrize
    async def test_raw_response_completion(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.inference.with_raw_response.completion(
            content="string",
            model="model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inference = await response.parse()
        assert_matches_type(InferenceCompletionResponse, inference, path=["response"])

    @parametrize
    async def test_streaming_response_completion(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.inference.with_streaming_response.completion(
            content="string",
            model="model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inference = await response.parse()
            assert_matches_type(InferenceCompletionResponse, inference, path=["response"])

        assert cast(Any, response.is_closed) is True