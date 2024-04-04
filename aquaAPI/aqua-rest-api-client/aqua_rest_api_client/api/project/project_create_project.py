from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_argument_error import ApiArgumentError
from ...models.api_backend_not_available_error import ApiBackendNotAvailableError
from ...models.api_forbidden_error import ApiForbiddenError
from ...models.api_internal_error import ApiInternalError
from ...models.api_project_create import ApiProjectCreate
from ...models.api_project_new_response import ApiProjectNewResponse
from ...models.api_unauthorized_error import ApiUnauthorizedError
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: ApiProjectCreate,
) -> Dict[str, Any]:
    url = "{}/api/Project".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
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
        ApiProjectNewResponse,
        ApiUnauthorizedError,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiProjectNewResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ApiArgumentError.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ApiForbiddenError.from_dict(response.json())

        return response_403
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
        ApiProjectNewResponse,
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
    *,
    client: AuthenticatedClient,
    json_body: ApiProjectCreate,
) -> Response[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiProjectNewResponse,
        ApiUnauthorizedError,
    ]
]:
    """Create project

     Create a new project with the given data - either from scratch (from default template)
                or as a copy of existing project. If required, items from source project are copied as
    well.
                (note the copy process is asynchronous - the email is send when it finishes).

    Args:
        json_body (ApiProjectCreate): Contains necessary information to create a new project.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiProjectNewResponse, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: ApiProjectCreate,
) -> Optional[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiProjectNewResponse,
        ApiUnauthorizedError,
    ]
]:
    """Create project

     Create a new project with the given data - either from scratch (from default template)
                or as a copy of existing project. If required, items from source project are copied as
    well.
                (note the copy process is asynchronous - the email is send when it finishes).

    Args:
        json_body (ApiProjectCreate): Contains necessary information to create a new project.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiProjectNewResponse, ApiUnauthorizedError]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: ApiProjectCreate,
) -> Response[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiProjectNewResponse,
        ApiUnauthorizedError,
    ]
]:
    """Create project

     Create a new project with the given data - either from scratch (from default template)
                or as a copy of existing project. If required, items from source project are copied as
    well.
                (note the copy process is asynchronous - the email is send when it finishes).

    Args:
        json_body (ApiProjectCreate): Contains necessary information to create a new project.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiProjectNewResponse, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: ApiProjectCreate,
) -> Optional[
    Union[
        ApiArgumentError,
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiProjectNewResponse,
        ApiUnauthorizedError,
    ]
]:
    """Create project

     Create a new project with the given data - either from scratch (from default template)
                or as a copy of existing project. If required, items from source project are copied as
    well.
                (note the copy process is asynchronous - the email is send when it finishes).

    Args:
        json_body (ApiProjectCreate): Contains necessary information to create a new project.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiArgumentError, ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiProjectNewResponse, ApiUnauthorizedError]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed