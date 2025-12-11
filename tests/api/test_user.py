import pytest
from pydantic import ValidationError, BaseModel
from pytest_mock import MockerFixture

from .user_schemas import UserResponseSchema
from ..mock_data.user_mock_data import MOCK_USER_RESPONSE


def validate_response_list(data: list[dict], schema: type[BaseModel]):
    try:
        return [schema(**item) for item in data]
    except ValidationError as e:
        pytest.fail(f"Pydantic validation error: {e}")


def test_valid_get_all_users(user_client):
    response = user_client.get_all_users()
    users_json = response.json()

    validated_users = validate_response_list(users_json, UserResponseSchema)

    assert response.status_code == 200
    assert isinstance(validated_users, list)
    assert len(validated_users) > 0
    assert validated_users[0].id == 1
    assert validated_users[-1].id == 10


def test_invalid_get_all_users(mocker: MockerFixture, user_client):
    mock_response = mocker.Mock()
    mock_response.json.return_value = MOCK_USER_RESPONSE
    mocker.patch.object(user_client, "get_all_users", return_value=mock_response)
    users_json = user_client.get_all_users().json()

    validate_response_list(users_json, UserResponseSchema)

