from pydantic import BaseModel


class BaseUser(BaseModel):
    id: int
    first_name: str
    last_name: str


class User(BaseUser):
    password: str
