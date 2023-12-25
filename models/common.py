from pydantic import BaseModel
from models.users import BaseUser


class AllUsersResponse(BaseModel):
    users: list[BaseUser]


class ActionResultResponse(BaseModel):
    result: bool
