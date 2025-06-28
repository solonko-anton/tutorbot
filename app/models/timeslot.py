from sqlmodel import SQLModel, Field
from datetime import datetime


class Timeslot(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    teacher_id: int | None = Field(foreign_key=None)
    student_id: int | None = Field(foreign_key=None)
    start_time: datetime = Field()
    end_time: datetime = Field()
