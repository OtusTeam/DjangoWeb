from db.session import Session
from models.genre import Genre
from models.movie import Movie
from models.review import Review


session = Session()
new_genre = Genre(name="Action")
session.add(new_genre)

new_genre = Genre(name="Fantasy")
session.add(new_genre)

new_genre = Genre(name="Mult")
session.add(new_genre)

new_genre = Genre(name="Melodrama")
session.add(new_genre)

session.commit()

session.close()

