"""Schemas for requests params"""

from pydantic import BaseModel, Field


class HelloParams(BaseModel):
    """Hello request params"""

    name: str | None = Field(pattern=r"^[^а-яА-Я]*$")
