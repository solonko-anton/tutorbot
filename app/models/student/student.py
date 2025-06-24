from sqlmodel import SQLModel, Field, Relationship


class Student(SQLModel, table=True):
    pass
