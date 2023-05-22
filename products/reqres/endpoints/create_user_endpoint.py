from core.base.base_endpoint import IEndpointTemplate
from products.reqres.testdata.user_test_data import create_user_request_payload
from core.utils.config_parser import get_endpoint
from core.constants.http_methods import HttpMethods


class CreateUserEndpoint(IEndpointTemplate):
    def url(self) -> str:
        return get_endpoint("create_user_endpoint")

    def http_method(self) -> str:
        return HttpMethods.POST.name

    def query_parameters(self) -> dict | None:
        return None

    def path_parameters(self) -> dict | None:
        return None

    def headers(self) -> dict:
        return {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def request_body(self) -> dict | None:
        return create_user_request_payload().dict()
