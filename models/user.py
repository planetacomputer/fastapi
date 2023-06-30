from pydantic import BaseModel


class User(BaseModel):
    id: int or None = None
    username: str


class UserIn(User):
    password: str
