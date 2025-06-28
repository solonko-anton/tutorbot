from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from app.models.user import User


class Complaint(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    author_id: int | None = Field(foreign_key="user.id")
    target_id: int | None = Field(foreign_key="user.id")
    author_type: str = Field()
    target_type: str = Field()
    reason: str = Field()
    description: str = Field()
    created_at: datetime = Field()
