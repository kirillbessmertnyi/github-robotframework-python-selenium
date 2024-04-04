from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_argument_error import ApiArgumentError
from ...models.api_backend_not_available_error import ApiBackendNotAvailableError
from ...models.api_forbidden_error import ApiForbiddenError
from ...models.api_internal_error import ApiInternalError
from ...models.api_not_found_error import ApiNotFoundError
from ...models.api_post_info import ApiPostInfo
from ...models.api_rich_text import ApiRichText
from ...models.api_unauthorized_error import ApiUnauthorizedError
from ...types import Response


def _get_kwargs(
    id: int,
    post_id: int,
    *,
    client: AuthenticatedClient,
    json_body: ApiRichText,
) -> Dict[str, Any]:
    url = "{}/api/Requirement/{id}/Post/{postId}".format(client.base_url, id=id, postId=post_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiPostInfo,
        ApiUnauthorizedError,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiPostInfo.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ApiArgumentError.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ApiForbiddenError.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ApiNotFoundError.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ApiUnauthorizedError.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ApiInternalError.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = ApiBackendNotAvailableError.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiPostInfo,
        ApiUnauthorizedError,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    post_id: int,
    *,
    client: AuthenticatedClient,
    json_body: ApiRichText,
) -> Response[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiPostInfo,
        ApiUnauthorizedError,
    ]
]:
    """Replace post

     Replace the existing post with id postId in the requirement with the given id.
                Users can be mentioned in the content with @UserName. The mentioned users
                will be extracted automatically. Only users which are members of the current requirement
                can be mentioned.

    Args:
        id (int):
        post_id (int):
        json_body (ApiRichText): Contains some rich text. The rich text is provided in several
            different formats.
            When sending rich text to the server, the rich text must be provided in exactly
            one format.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiPostInfo, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        id=id,
        post_id=post_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    post_id: int,
    *,
    client: AuthenticatedClient,
    json_body: ApiRichText,
) -> Optional[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiPostInfo,
        ApiUnauthorizedError,
    ]
]:
    """Replace post

     Replace the existing post with id postId in the requirement with the given id.
                Users can be mentioned in the content with @UserName. The mentioned users
                will be extracted automatically. Only users which are members of the current requirement
                can be mentioned.

    Args:
        id (int):
        post_id (int):
        json_body (ApiRichText): Contains some rich text. The rich text is provided in several
            different formats.
            When sending rich text to the server, the rich text must be provided in exactly
            one format.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiPostInfo, ApiUnauthorizedError]]
    """

    return sync_detailed(
        id=id,
        post_id=post_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    id: int,
    post_id: int,
    *,
    client: AuthenticatedClient,
    json_body: ApiRichText,
) -> Response[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiPostInfo,
        ApiUnauthorizedError,
    ]
]:
    """Replace post

     Replace the existing post with id postId in the requirement with the given id.
                Users can be mentioned in the content with @UserName. The mentioned users
                will be extracted automatically. Only users which are members of the current requirement
                can be mentioned.

    Args:
        id (int):
        post_id (int):
        json_body (ApiRichText): Contains some rich text. The rich text is provided in several
            different formats.
            When sending rich text to the server, the rich text must be provided in exactly
            one format.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiPostInfo, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        id=id,
        post_id=post_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    post_id: int,
    *,
    client: AuthenticatedClient,
    json_body: ApiRichText,
) -> Optional[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiPostInfo,
        ApiUnauthorizedError,
    ]
]:
    """Replace post

     Replace the existing post with id postId in the requirement with the given id.
                Users can be mentioned in the content with @UserName. The mentioned users
                will be extracted automatically. Only users which are members of the current requirement
                can be mentioned.

    Args:
        id (int):
        post_id (int):
        json_body (ApiRichText): Contains some rich text. The rich text is provided in several
            different formats.
            When sending rich text to the server, the rich text must be provided in exactly
            one format.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiPostInfo, ApiUnauthorizedError]]
    """

    return (
        await asyncio_detailed(
            id=id,
            post_id=post_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
