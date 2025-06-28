from sqlmodel import SQLModel, Field, Relationship
from app.models.user import User


class TeacherDirectionLink(SQLModel, table=True):
    teacher_id: int | None = Field(
        default=None, foreign_key="teacher.id", primary_key=True
    )
    direction_id: int | None = Field(
        default=None, foreign_key="direction.id", primary_key=True
    )


class TeacherLessonsLink(SQLModel, table=True):
    teacher_id: int | None = Field(
        default=None, foreign_key="teacher.id", primary_key=True
    )
    lesson_id: int | None = Field(
        default=None, foreign_key="lesson.id", primary_key=True
    )


class Teacher(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int | None = Field(foreign_key="user.id")
    verified: bool = Field()
    city: str = Field()
    years_expirience: float = Field()
    description: str = Field(max_length=255)

    lessons: list["Lesson"] = Relationship(
        back_populates="teachers", link_model=TeacherLessonsLink
    )
    directions: list["Direction"] = Relationship(
        back_populates="teachers", link_model=TeacherDirectionLink
    )


class Lesson(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field()
    price: int = Field()

    teachers: list["Teacher"] = Relationship(
        back_populates="lessons", link_model=TeacherLessonsLink
    )


class Direction(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field()

    teachers: list["Teacher"] = Relationship(
        back_populates="directions", link_model=TeacherDirectionLink
    )
