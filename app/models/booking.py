from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from app.models.profiles.student import Student
from app.models.timeslot import Timeslot
from app.models.profiles.teacher import Lesson


class Booking(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    student_id: int | None = Field(
        default=None, foreign_key="student.id", primary_key=True
    )
    timeslot_id: int | None = Field(
        default=None, foreign_key="timeslot.id", primary_key=True
    )
    lesson_id: int | None = Field(
        default=None, foreign_key="lesson.id", primary_key=True
    )
    booked_at: datetime = Field()
