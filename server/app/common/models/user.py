from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import date


class CreateUser(SQLModel):
    name: str
    surname: str
    salary: int
    position: str
    hire_date: str = Field(default=str(date.today()))
    boss_id: Optional[int] = Field(default=None, nullable=True)


class User(CreateUser, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class UpdateUser(SQLModel):
    name: Optional[str]
    surname: Optional[str]
    salary: Optional[int]
    position: Optional[str]
    boss_id: Optional[int]
