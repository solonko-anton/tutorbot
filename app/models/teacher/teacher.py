from sqlmodel import SQLModel, Field, Relationship
from app.models.teacher.direction import Direction
from app.models.teacher.lesson import Lesson


class Teacher(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    tg_id: int = Field()
    name: str = Field()
    surname: str = Field()
    patronymic: str = Field()
    verified: bool = Field()
    city: str = Field()
    years_expirience: float = Field()
    description: str = Field(max_length=255)

    lessons: list["Lesson"] = Relationship(back_populates="teachers", link_model="TeacherLessonsLink")
    directions: list["Direction"] = Relationship(back_populates="teachers", link_model="TeacherDirectionLink")    


class TeacherDirectionLink(SQLModel, table=True):
    teacher_id: int | None = Field(default=None, foreign_key="teacher.id", primary_key=True)
    direction_id: int | None = Field(default=None, foreign_key="direction.id", primary_key=True)


class TeacherLessonsLink(SQLModel, table=True):
    teacher_id: int | None = Field(default=None, foreign_key="teacher.id", primary_key=True)
    lesson_id: int | None = Field(default=None, foreign_key="lesson.id", primary_key=True)

