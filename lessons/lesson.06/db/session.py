from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import DATABASE_URL


# Создаем движок
engine = create_engine(DATABASE_URL, echo=True)

# Создаем базовый класс
Base = declarative_base()

# Фабрика сессия
Session = sessionmaker(bind=engine)