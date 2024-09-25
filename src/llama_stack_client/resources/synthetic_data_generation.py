# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..types import synthetic_data_generation_generate_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.synthetic_data_generation import SyntheticDataGeneration

__all__ = ["SyntheticDataGenerationResource", "AsyncSyntheticDataGenerationResource"]


class SyntheticDataGenerationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SyntheticDataGenerationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return SyntheticDataGenerationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SyntheticDataGenerationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return SyntheticDataGenerationResourceWithStreamingResponse(self)

    def generate(
        self,
        *,
        dialogs: Iterable[synthetic_data_generation_generate_params.Dialog],
        filtering_function: Literal["none", "random", "top_k", "top_p", "top_k_top_p", "sigmoid"],
        model: str | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyntheticDataGeneration:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"X-LlamaStack-ProviderData": x_llama_stack_provider_data}),
            **(extra_headers or {}),
        }
        return self._post(
            "/synthetic_data_generation/generate",
            body=maybe_transform(
                {
                    "dialogs": dialogs,
                    "filtering_function": filtering_function,
                    "model": model,
                },
                synthetic_data_generation_generate_params.SyntheticDataGenerationGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SyntheticDataGeneration,
        )


class AsyncSyntheticDataGenerationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSyntheticDataGenerationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSyntheticDataGenerationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSyntheticDataGenerationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return AsyncSyntheticDataGenerationResourceWithStreamingResponse(self)

    async def generate(
        self,
        *,
        dialogs: Iterable[synthetic_data_generation_generate_params.Dialog],
        filtering_function: Literal["none", "random", "top_k", "top_p", "top_k_top_p", "sigmoid"],
        model: str | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyntheticDataGeneration:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"X-LlamaStack-ProviderData": x_llama_stack_provider_data}),
            **(extra_headers or {}),
        }
        return await self._post(
            "/synthetic_data_generation/generate",
            body=await async_maybe_transform(
                {
                    "dialogs": dialogs,
                    "filtering_function": filtering_function,
                    "model": model,
                },
                synthetic_data_generation_generate_params.SyntheticDataGenerationGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SyntheticDataGeneration,
        )


class SyntheticDataGenerationResourceWithRawResponse:
    def __init__(self, synthetic_data_generation: SyntheticDataGenerationResource) -> None:
        self._synthetic_data_generation = synthetic_data_generation

        self.generate = to_raw_response_wrapper(
            synthetic_data_generation.generate,
        )


class AsyncSyntheticDataGenerationResourceWithRawResponse:
    def __init__(self, synthetic_data_generation: AsyncSyntheticDataGenerationResource) -> None:
        self._synthetic_data_generation = synthetic_data_generation

        self.generate = async_to_raw_response_wrapper(
            synthetic_data_generation.generate,
        )


class SyntheticDataGenerationResourceWithStreamingResponse:
    def __init__(self, synthetic_data_generation: SyntheticDataGenerationResource) -> None:
        self._synthetic_data_generation = synthetic_data_generation

        self.generate = to_streamed_response_wrapper(
            synthetic_data_generation.generate,
        )


class AsyncSyntheticDataGenerationResourceWithStreamingResponse:
    def __init__(self, synthetic_data_generation: AsyncSyntheticDataGenerationResource) -> None:
        self._synthetic_data_generation = synthetic_data_generation

        self.generate = async_to_streamed_response_wrapper(
            synthetic_data_generation.generate,
        )