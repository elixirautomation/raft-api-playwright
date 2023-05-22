from pydantic import BaseModel


class CreateUserResponse(BaseModel):
    name: str
    job: str
    id: str
    createdAt: str
