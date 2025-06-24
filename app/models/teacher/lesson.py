from sqlmodel import SQLModel, Field, Relationship
from app.models.teacher.teacher import Teacher
from app.models.teacher.teacher import TeacherLessonsLink


class Lesson(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field()
    price: int = Field()

    teachers: list["Teacher"] = Relationship(back_populates="lessons", link_model="TeacherLessonsLink")