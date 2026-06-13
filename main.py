from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Create the app
app = FastAPI()

# Define what a User looks like
class User(BaseModel):
    name: str
    email: str

# Fake database (just a list for now)
fake_db = []

# GET all users - Returns 200 automatically
@app.get("/users")
def get_users():
    return {"status": "success", "data": fake_db}

# GET single user by ID - Returns 404 if not found
@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id < 0 or user_id >= len(fake_db):
        raise HTTPException(status_code=404, detail="User not found")
    return {"status": "success", "data": fake_db[user_id]}

# POST create new user - Returns 201 on success, 400 on bad data
@app.post("/users", status_code=201)
def create_user(user: User):
    if not user.name.strip() or not user.email.strip():
        raise HTTPException(status_code=400, detail="Name and email cannot be empty")
    if "@" not in user.email:
        raise HTTPException(status_code=400, detail="Invalid email address")
    fake_db.append(user)
    return {"status": "created", "data": user}