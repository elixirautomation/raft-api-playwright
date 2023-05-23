from products.reqres.models.requests.user_request import UserRequest
from faker import Faker

data_generator = Faker()


def create_user_request_payload() -> UserRequest:
    random_name = data_generator.name()
    random_job = data_generator.job()
    return UserRequest(name=random_name, job=random_job)
