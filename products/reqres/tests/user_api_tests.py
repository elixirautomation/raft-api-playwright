import pytest
from allure import description, epic, story, step
from core.utils.logger_config import get_logger
from products.reqres.clients.user_client import UserClient
from assertpy.assertpy import assert_that
from http import HTTPStatus


@epic("User Acquisition")
@story("Test User Modules")
@description("Scenarios: user creation & result verification")
class TestUserModules:
    logger = get_logger(module_name=__name__)

    @pytest.fixture(scope="module")
    def user_ids(self):
        ids: list = []
        yield ids

    @pytest.fixture
    def user_client(self, request_context):
        user_client_context = UserClient(request_context=request_context)
        yield user_client_context

    @step("Create a user")
    @pytest.mark.reqres
    @pytest.mark.dependency()
    def test_create_user(self, user_client, user_ids):
        status_code, response = user_client.create_user()
        assert_that(status_code).is_equal_to(HTTPStatus.CREATED)
        assert_that(response.id).is_not_none()
        user_ids.append(response.id)

    @step("Get a user profile which doesn't exist")
    @pytest.mark.reqres
    @pytest.mark.dependency(depends=['TestUserModules::test_create_user'])
    def test_get_user_not_found(self, user_client, user_ids):
        status_code, response = user_client.get_user(user_id=user_ids[0])
        assert_that(status_code).is_equal_to(HTTPStatus.NOT_FOUND)

    @step("Get a valid user profile")
    @pytest.mark.reqres
    @pytest.mark.dependency()
    def test_get_user_happy_flow(self, user_client):
        status_code, response = user_client.get_user(user_id="2")
        assert_that(status_code).is_equal_to(HTTPStatus.OK)
        assert_that(response.data.id).is_equal_to(2)
