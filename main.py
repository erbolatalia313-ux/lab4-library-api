from fastapi import FastAPI, HTTPException

app = FastAPI()

books = [
    {"id": 1, "title": "Абай жолы", "author": "М. Әуезов", "year": 1942},
    {"id": 2, "title": "Махаббат қызық мол жылдар", "author": "Ә. Нұршайықов", "year": 1960}
]

@app.get("/books")
def get_books():
    return books

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Кітап табылмады")

@app.post("/books")
def add_book(book: dict):
    new_id = max([b["id"] for b in books]) + 1 if books else 1
    book["id"] = new_id
    books.append(book)
    return book

@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: dict):
    for i, book in enumerate(books):
        if book["id"] == book_id:
            books[i].update(updated_book)
            return books[i]
    raise HTTPException(status_code=404, detail="Кітап табылмады")

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for i, book in enumerate(books):
        if book["id"] == book_id:
            return books.pop(i)
    raise HTTPException(status_code=404, detail="Кітап табылмады")
