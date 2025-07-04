from sqlmodel import SQLModel, Field, Relationship


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    tg_id: int = Field()
    username: str = Field()
    first_name: str = Field()
    last_name: str = Field()
    phone: str = Field()
    patronymic: str = Field()
    country: str = Field()
    city: str = Field()
