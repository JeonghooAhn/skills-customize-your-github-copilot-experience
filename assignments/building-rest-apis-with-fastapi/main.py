from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Reading List API")


class BookInput(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    year: int = Field(gt=0)


class Book(BookInput):
    id: int


books: list[Book] = []


@app.get("/books", response_model=list[Book])
def list_books() -> list[Book]:
    return books


# TODO: Add POST /books, GET /books/{book_id}, PUT /books/{book_id},
# and DELETE /books/{book_id}.
