import uvicorn
from fastapi import FastAPI, HTTPException, Query, Depends, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional
from db.session import get_db
from schemas.movie import Movie, MovieId
from sqlalchemy.orm import Session as MySession
from crud.movie import create_movie, get_movies
from api.movies import router as movies_router

#
# class Movie(BaseModel):
#     title: str
#     year: int
#     description: str
#
#
# class MovieId(Movie):
#     id: int


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

list_movies = [
    Movie(
        title="Movie_1",
        year=1999,
        description="Movie_description",
    ),
    Movie(
        title="Movie_2",
        year=1992,
        description="Movie description 2",
    ),
    Movie(
        title="Movie_3",
        year=1929,
        description="Movie description 3",
    ),
    Movie(
        title="Movie_1",
        year=1929,
        description="Movie description 3",
    ),
]


@app.get("/")
async def index(request: Request):
    # context = {"request": request}
    # return {"Кинотеатр": "Movies"}
    return templates.TemplateResponse("index.html", {"request": request, "title": "Наша страница", "movies": list_movies})

@app.get("/movies/")
async def get_movies(
    year: Optional[int] = Query(None, description="Год выпуска"),
    title: Optional[str] = Query(None, description="Наименование"),
):
    result = list_movies
    if year is not None:
        result = [movie for movie in result if movie.year == year]

    print(year)
    print(result)

    if title is not None:
        result = [movie for movie in result if title.lower() in movie.title.lower()]
    print(title)
    print(result)

    return result



@app.get("/movies/{movie_id}")
async def get_movie_id(movie_id: int):
    if movie_id < 0 or movie_id > len(list_movies):
        raise HTTPException(status_code=404, detail="Нет фильма с таким id")
    return list_movies[movie_id]


@app.post("/movies/")
async def get_movies(movie: Movie):
    for m in list_movies:
        if m.title == movie.title and m.year == movie.year:
            raise HTTPException(status_code=404, detail="Такой фильм уже есть")

    list_movies.append(movie)
    return movie


@app.put("/movies/{movie_id}")
async def put_movie_id(movie_id: int, new_movie: Movie):
    if movie_id < 0 or movie_id > len(list_movies):
        raise HTTPException(status_code=404, detail="Нет фильма с таким id")
    list_movies[movie_id].title = new_movie.title
    list_movies[movie_id].year = new_movie.year
    list_movies[movie_id].description = new_movie.description

    return list_movies[movie_id]


@app.delete("/movies/{movie_id}")
async def delete_movie_id(movie_id: int):
    if movie_id < 0 or movie_id > len(list_movies):
        raise HTTPException(status_code=404, detail="Нет фильма с таким id")
    res = list_movies.pop(movie_id)
    return {'message': f'Фильм {res.title} удален'}


@app.get("/movies_db/")
async def get_movies(db: MySession = Depends(get_db)):
    movies = get_movies(db)

    return movies


app.include_router(movies_router)

# Запуск
if __name__ == '__main__':
    uvicorn.run("app:app", port=8000, reload=True)