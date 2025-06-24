from sqlmodel import SQLModel, Field, Relationship


class Student(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)


