from pydantic import BaseModel, Field


class Movie(BaseModel):
    title: str = Field(..., example='Matrix', description='Movie title')
    year: int = Field(..., example=1999, description='Year of release')
    description: str = Field(..., example="Matrix description", description='Movie description')


class MovieId(Movie):
    id: int = Field(..., example=1,  description='Movie ID')