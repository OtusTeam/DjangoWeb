from fastapi import APIRouter, HTTPException, Query, Depends, status
from typing import Optional
from db.session import get_db
from schemas.movie import Movie, MovieId
from sqlalchemy.orm import Session as MySession
from crud.movie import create_movie, get_movies


router = APIRouter(
    prefix="/moviesdb",
    tags=["moviesdb"]
)


@router.post(
    "/",
    response_model=Movie,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new movie",
    description="Create a new movie 1111"
)
def add_movie(movie_in: Movie, db: MySession = Depends(get_db)):
    movie = create_movie(db, movie_in)
    return movie
