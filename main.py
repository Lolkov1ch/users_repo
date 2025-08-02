from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models.users import User
from models.users import UserCreate
from db import init_db, get_all_users, get_user_by_id, insert_user

app = FastAPI()
init_db()

@app.get("/users")
def get_users():
    users_data = get_all_users()
    return [User(user_id=row[0], username=row[1], email=row[2]) for row in users_data]

@app.get("/users/{user_id}")
def get_user(user_id: int):
    row = get_user_by_id(user_id)
    if row:
        return User(user_id=row[0], username=row[1], email=row[2])
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/create_user")
def create_user(user: UserCreate):
    user_id = insert_user(user.username, user.email)
    if user_id is None:
        raise HTTPException(status_code=500, detail="Failed to create user")
    return User(user_id=user_id, username=user.username, email=user.email)
