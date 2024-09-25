# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal

import httpx

from .jobs import (
    JobsResource,
    AsyncJobsResource,
    JobsResourceWithRawResponse,
    AsyncJobsResourceWithRawResponse,
    JobsResourceWithStreamingResponse,
    AsyncJobsResourceWithStreamingResponse,
)
from ...types import (
    post_training_preference_optimize_params,
    post_training_supervised_fine_tune_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.post_training_job import PostTrainingJob
from ...types.train_eval_dataset_param import TrainEvalDatasetParam

__all__ = ["PostTrainingResource", "AsyncPostTrainingResource"]


class PostTrainingResource(SyncAPIResource):
    @cached_property
    def jobs(self) -> JobsResource:
        return JobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PostTrainingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return PostTrainingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PostTrainingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return PostTrainingResourceWithStreamingResponse(self)

    def preference_optimize(
        self,
        *,
        algorithm: Literal["dpo"],
        algorithm_config: post_training_preference_optimize_params.AlgorithmConfig,
        dataset: TrainEvalDatasetParam,
        finetuned_model: str,
        hyperparam_search_config: Dict[str, Union[bool, float, str, Iterable[object], object, None]],
        job_uuid: str,
        logger_config: Dict[str, Union[bool, float, str, Iterable[object], object, None]],
        optimizer_config: post_training_preference_optimize_params.OptimizerConfig,
        training_config: post_training_preference_optimize_params.TrainingConfig,
        validation_dataset: TrainEvalDatasetParam,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PostTrainingJob:
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
            "/post_training/preference_optimize",
            body=maybe_transform(
                {
                    "algorithm": algorithm,
                    "algorithm_config": algorithm_config,
                    "dataset": dataset,
                    "finetuned_model": finetuned_model,
                    "hyperparam_search_config": hyperparam_search_config,
                    "job_uuid": job_uuid,
                    "logger_config": logger_config,
                    "optimizer_config": optimizer_config,
                    "training_config": training_config,
                    "validation_dataset": validation_dataset,
                },
                post_training_preference_optimize_params.PostTrainingPreferenceOptimizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostTrainingJob,
        )

    def supervised_fine_tune(
        self,
        *,
        algorithm: Literal["full", "lora", "qlora", "dora"],
        algorithm_config: post_training_supervised_fine_tune_params.AlgorithmConfig,
        dataset: TrainEvalDatasetParam,
        hyperparam_search_config: Dict[str, Union[bool, float, str, Iterable[object], object, None]],
        job_uuid: str,
        logger_config: Dict[str, Union[bool, float, str, Iterable[object], object, None]],
        model: str,
        optimizer_config: post_training_supervised_fine_tune_params.OptimizerConfig,
        training_config: post_training_supervised_fine_tune_params.TrainingConfig,
        validation_dataset: TrainEvalDatasetParam,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PostTrainingJob:
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
            "/post_training/supervised_fine_tune",
            body=maybe_transform(
                {
                    "algorithm": algorithm,
                    "algorithm_config": algorithm_config,
                    "dataset": dataset,
                    "hyperparam_search_config": hyperparam_search_config,
                    "job_uuid": job_uuid,
                    "logger_config": logger_config,
                    "model": model,
                    "optimizer_config": optimizer_config,
                    "training_config": training_config,
                    "validation_dataset": validation_dataset,
                },
                post_training_supervised_fine_tune_params.PostTrainingSupervisedFineTuneParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostTrainingJob,
        )


class AsyncPostTrainingResource(AsyncAPIResource):
    @cached_property
    def jobs(self) -> AsyncJobsResource:
        return AsyncJobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPostTrainingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPostTrainingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPostTrainingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return AsyncPostTrainingResourceWithStreamingResponse(self)

    async def preference_optimize(
        self,
        *,
        algorithm: Literal["dpo"],
        algorithm_config: post_training_preference_optimize_params.AlgorithmConfig,
        dataset: TrainEvalDatasetParam,
        finetuned_model: str,
        hyperparam_search_config: Dict[str, Union[bool, float, str, Iterable[object], object, None]],
        job_uuid: str,
        logger_config: Dict[str, Union[bool, float, str, Iterable[object], object, None]],
        optimizer_config: post_training_preference_optimize_params.OptimizerConfig,
        training_config: post_training_preference_optimize_params.TrainingConfig,
        validation_dataset: TrainEvalDatasetParam,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PostTrainingJob:
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
            "/post_training/preference_optimize",
            body=await async_maybe_transform(
                {
                    "algorithm": algorithm,
                    "algorithm_config": algorithm_config,
                    "dataset": dataset,
                    "finetuned_model": finetuned_model,
                    "hyperparam_search_config": hyperparam_search_config,
                    "job_uuid": job_uuid,
                    "logger_config": logger_config,
                    "optimizer_config": optimizer_config,
                    "training_config": training_config,
                    "validation_dataset": validation_dataset,
                },
                post_training_preference_optimize_params.PostTrainingPreferenceOptimizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostTrainingJob,
        )

    async def supervised_fine_tune(
        self,
        *,
        algorithm: Literal["full", "lora", "qlora", "dora"],
        algorithm_config: post_training_supervised_fine_tune_params.AlgorithmConfig,
        dataset: TrainEvalDatasetParam,
        hyperparam_search_config: Dict[str, Union[bool, float, str, Iterable[object], object, None]],
        job_uuid: str,
        logger_config: Dict[str, Union[bool, float, str, Iterable[object], object, None]],
        model: str,
        optimizer_config: post_training_supervised_fine_tune_params.OptimizerConfig,
        training_config: post_training_supervised_fine_tune_params.TrainingConfig,
        validation_dataset: TrainEvalDatasetParam,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PostTrainingJob:
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
            "/post_training/supervised_fine_tune",
            body=await async_maybe_transform(
                {
                    "algorithm": algorithm,
                    "algorithm_config": algorithm_config,
                    "dataset": dataset,
                    "hyperparam_search_config": hyperparam_search_config,
                    "job_uuid": job_uuid,
                    "logger_config": logger_config,
                    "model": model,
                    "optimizer_config": optimizer_config,
                    "training_config": training_config,
                    "validation_dataset": validation_dataset,
                },
                post_training_supervised_fine_tune_params.PostTrainingSupervisedFineTuneParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostTrainingJob,
        )


class PostTrainingResourceWithRawResponse:
    def __init__(self, post_training: PostTrainingResource) -> None:
        self._post_training = post_training

        self.preference_optimize = to_raw_response_wrapper(
            post_training.preference_optimize,
        )
        self.supervised_fine_tune = to_raw_response_wrapper(
            post_training.supervised_fine_tune,
        )

    @cached_property
    def jobs(self) -> JobsResourceWithRawResponse:
        return JobsResourceWithRawResponse(self._post_training.jobs)


class AsyncPostTrainingResourceWithRawResponse:
    def __init__(self, post_training: AsyncPostTrainingResource) -> None:
        self._post_training = post_training

        self.preference_optimize = async_to_raw_response_wrapper(
            post_training.preference_optimize,
        )
        self.supervised_fine_tune = async_to_raw_response_wrapper(
            post_training.supervised_fine_tune,
        )

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithRawResponse:
        return AsyncJobsResourceWithRawResponse(self._post_training.jobs)


class PostTrainingResourceWithStreamingResponse:
    def __init__(self, post_training: PostTrainingResource) -> None:
        self._post_training = post_training

        self.preference_optimize = to_streamed_response_wrapper(
            post_training.preference_optimize,
        )
        self.supervised_fine_tune = to_streamed_response_wrapper(
            post_training.supervised_fine_tune,
        )

    @cached_property
    def jobs(self) -> JobsResourceWithStreamingResponse:
        return JobsResourceWithStreamingResponse(self._post_training.jobs)


class AsyncPostTrainingResourceWithStreamingResponse:
    def __init__(self, post_training: AsyncPostTrainingResource) -> None:
        self._post_training = post_training

        self.preference_optimize = async_to_streamed_response_wrapper(
            post_training.preference_optimize,
        )
        self.supervised_fine_tune = async_to_streamed_response_wrapper(
            post_training.supervised_fine_tune,
        )

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithStreamingResponse:
        return AsyncJobsResourceWithStreamingResponse(self._post_training.jobs)