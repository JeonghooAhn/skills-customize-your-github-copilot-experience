# 📘 Assignment: Testing and Debugging Python APIs

## 🎯 Objective

Practice writing automated tests with `pytest` and using test failures to find and fix bugs in a FastAPI application. This assignment builds on the Reading List API from the Building REST APIs with FastAPI assignment.

## 📝 Tasks

### 🛠️ Write Your First API Tests

#### Description
Use the completed Reading List API project as the program to test. Install `pytest`, create a `tests/test_main.py` file, and use FastAPI's `TestClient` to send requests without starting a server.

#### Requirements
Completed program should:

- Install `pytest` in the same environment as the FastAPI project
- Create a `TestClient` for the FastAPI app
- Test that `GET /books` returns an empty list when no books have been added
- Test that `POST /books` creates a book with the expected fields and a `201 Created` response
- Run the tests with `pytest -q` and confirm they pass


### 🛠️ Test Errors and Edge Cases

#### Description
Expand the test suite to cover invalid input and requests for books that do not exist. Check both the HTTP status code and the useful parts of each response.

#### Requirements
Completed program should:

- Test that a book with an empty title, empty author, or non-positive year is rejected with a `422` response
- Test that retrieving, updating, or deleting an unknown book ID returns `404`
- Check that successful update and delete requests change the collection as expected
- Reset the in-memory books collection for each test so tests pass regardless of their run order


### 🛠️ Debug a Failing Test

#### Description
Run the full test suite, use the failure output to locate a bug in the API, and correct the implementation. Add a regression test so the same bug is caught if it returns later.

#### Requirements
Completed program should:

- Use a failing assertion and its traceback to identify the request or response that is incorrect
- Fix the API behavior rather than weakening or deleting a failing test
- Add a test that reproduces the bug before the fix
- Run `pytest -q` again and confirm that all tests pass