from sqlmodel import SQLModel, Field, Relationship
from app.models.user import User


class Student(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int | None = Field(foreign_key="user.id")
