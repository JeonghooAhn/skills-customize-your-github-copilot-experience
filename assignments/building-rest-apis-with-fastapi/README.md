# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small Reading List API with FastAPI. You will practice defining HTTP endpoints, validating request data with Pydantic, and returning appropriate responses for a resource.

## 🧰 Setup

Use Python 3.10 or later. Download `main.py` from the assignment attachments, then create and activate a virtual environment and install FastAPI:

```bash
python -m venv .venv
```

Install the packages and start the development server:

```bash
python -m pip install "fastapi[standard]"
uvicorn main:app --reload
```

Keep the server running while you try the API at `http://127.0.0.1:8000/docs`.

## 📝 Tasks

### 🛠️ List Books

#### Description
Start the application and use its books collection endpoint to see the reading list. Books should be stored in memory while the server is running.

#### Requirements
Completed program should:

- Start as a FastAPI application titled `Reading List API`
- Provide `GET /books` that returns the current list of books (initially an empty list)
- Return each book as JSON with an integer `id`, a `title`, an `author`, and a publication `year`


### 🛠️ Add and Validate Books

#### Description
Create a Pydantic model for incoming book data and add an endpoint for creating a book. Let FastAPI validate the request body.

#### Requirements
Completed program should:

- Provide `POST /books` that accepts a JSON body containing `title`, `author`, and `year`
- Require non-empty titles and authors, and require the year to be a positive integer
- Assign a unique integer ID, store the new book, and return it with HTTP status `201 Created`
- Return FastAPI's validation response for invalid request data


### 🛠️ Retrieve, Update, and Delete Books

#### Description
Add endpoints to manage a book by its ID. If an ID is not in the collection, return a clear `404 Not Found` response.

#### Requirements
Completed program should:

- Provide `GET /books/{book_id}` to return one book
- Provide `PUT /books/{book_id}` to replace a book's title, author, and year using the same validation rules
- Provide `DELETE /books/{book_id}` to remove a book
- Return HTTP `404 Not Found` when any of these operations refers to a book that does not exist


### 🛠️ Try the API

#### Description
Run the server and use FastAPI's interactive documentation to exercise each endpoint.

#### Requirements
Completed program should:

- Use `http://127.0.0.1:8000/docs` to create, list, retrieve, update, and delete a book
- Confirm that invalid input is rejected and an unknown book ID returns `404`
- Confirm that the list reflects successful changes while the server is running
