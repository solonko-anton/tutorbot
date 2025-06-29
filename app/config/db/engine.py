import os
from sqlmodel import SQLModel, create_engine
from dotenv import load_dotenv

load_dotenv()

db_url = os.getenv("DATABASE_URL")

engine = create_engine(db_url, echo=True)
