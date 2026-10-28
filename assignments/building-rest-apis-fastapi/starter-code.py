from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field

app = FastAPI(title="Book API")


class BookInput(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)


class Book(BookInput):
    id: int


books: list[Book] = [
    Book(id=1, title="The Hobbit", author="J. R. R. Tolkien"),
    Book(id=2, title="Frankenstein", author="Mary Shelley"),
]
next_book_id = 3


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Book API is running"}


# TODO: Add GET /books to return the complete collection.
# TODO: Add POST /books to validate and create a book.
# TODO: Add GET, PUT, and DELETE routes for /books/{book_id}.
# Return HTTP 404 when a book ID does not exist.
