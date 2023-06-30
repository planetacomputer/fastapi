from pydantic import BaseModel


class UserPostIn(BaseModel):
    body: str
    user_id: int


class UserPost(UserPostIn):
    id: int
