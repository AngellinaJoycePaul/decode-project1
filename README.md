# Project 1: REST API Fundamentals
**Decode Labs Backend Development Internship**
Built by: Angellina Joyce Paul

## 📌 About
A stateless REST API built with Python and FastAPI.
Demonstrates GET and POST routes with proper HTTP status codes.

## 🛠️ Tech Stack
- Python 3.14
- FastAPI
- Uvicorn

## 🚀 How to Run
1. Create virtual environment
   python -m venv venv
   venv\Scripts\activate

2. Install dependencies
   pip install fastapi uvicorn

3. Run the server
   uvicorn main:app --reload

4. Open docs at
   http://127.0.0.1:8000/docs

## 📡 API Routes
| Method | Route | Description | Status Code |
|--------|-------|-------------|-------------|
| GET | /users | Get all users | 200 |
| GET | /users/{id} | Get single user | 200 / 404 |
| POST | /users | Create new user | 201 / 400 |

## 📸 Screenshots

### Swagger UI Homepage
![Swagger UI](screenshots/1_swagger_ui.png)

### POST /users — 201 Created
![201 Created](screenshots/2_post_201.png)

### GET /users — 200 OK
![200 OK](screenshots/3_get_200.png)

### GET /users/99 — 404 Not Found
![404 Not Found](screenshots/4_get_404.png)

### POST /users — 400 Bad Request
![400 Bad Request](screenshots/5_post_400.png)