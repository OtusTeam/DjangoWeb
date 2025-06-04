from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session as MySession
from config import DATABASE_URL
from typing import Generator

# Создаем движок
engine = create_engine(DATABASE_URL, echo=True)

# Создаем базовый класс
Base = declarative_base()

# Фабрика сессия
Session = sessionmaker(bind=engine)


def get_db() -> Generator[MySession, None, None]:
    db = Session()
    try:
        yield db
    finally:
        db.close()
