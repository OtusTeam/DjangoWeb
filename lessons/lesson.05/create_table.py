from db.session import engine, Base
from models.genre import Genre
from models.movie import Movie
from models.review import Review


if __name__ == '__main__':
    print('Создаем таблицы')
    Base.metadata.create_all(engine)
    print('Готово! Создал таблицы')

