import json
from core.utils.logger_config import get_logger
from core.base.base_client import BaseClient
from products.reqres.models.responses.get_user_response import UserResponse
from products.reqres.models.responses.create_user_response import CreateUserResponse
from playwright.sync_api import APIRequestContext
from products.reqres.endpoints.create_user_endpoint import CreateUserEndpoint
from products.reqres.endpoints.get_user_endpoint import GetUserEndpoint


class UserClient(BaseClient):

    def __init__(self, request_context: APIRequestContext):
        super().__init__(request_context)
        self.logger = get_logger(module_name=__name__)
        self.create_user_endpoint = CreateUserEndpoint()
        self.get_user_endpoint = GetUserEndpoint()

    def create_user(self) -> (int, dict):
        status_code, response = self.request_processor(self.create_user_endpoint)
        self.logger.info("\nCreate User Response:\n{}".format(json.dumps(response, indent=4)))
        user_response = CreateUserResponse.parse_obj(response)
        return status_code, user_response

    def get_user(self, user_id: str) -> (int, dict):
        status_code, response = self.request_processor(self.get_user_endpoint, user_id=user_id)
        self.logger.info("\nGet User Response:\n{}".format(json.dumps(response, indent=4)))
        if response != {}:
            user_response = UserResponse.parse_obj(response)
            return status_code, user_response
        else:
            return status_code, response
