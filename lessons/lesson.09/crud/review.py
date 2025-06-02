# from sqlalchemy.orm import Session
# from  models.review import Review
# from models.genre import Genre
# from models.review import Review
# from schemas.movie import MovieId, Movie,
#
#
# def create_movie(db: Session, movie_in: Movie) -> Movie:
#     movie = Movie(
#         title=movie_in.title,
#         year=movie_in.year,
#         description=movie_in.description,
#     )
#     db.add(movie)
#     db.commit()
#     db.refresh(movie)
#     return movie
#
#
# def get_movies(db: Session, skip: int = 0, limit: int = 100) -> list[Movie]:
#     return db.query(Movie).offset(skip).limit(limit).all()
