from pydantic import BaseModel


class List(BaseModel):
    username: str = None
    body: str = None
    status: bool = False