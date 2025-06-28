from sqlmodel import SQLModel, Field, Relationship


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field()
    first_name: str = Field()
    last_name: str = Field()
    phone: str = Field()
    patronymic: str = Field()
