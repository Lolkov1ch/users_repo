from fastapi import FastAPI
from models.users import User


app = FastAPI()


users = [
    User(user_id=1, username="john_doe", email="john_doe@gmail.com"),
    User(user_id=2, username="андрій", email="andriy@gmail.com"),
    User(user_id=3, username="максим", email="maxim@gmail.com"),
    User(user_id=4, username="артем", email="artem@gmail.com"),
    User(user_id=5, username="анатолій", email="anatoliy@gmail.com")
]

@app.get("/users")
def get_all_users():
    return users

@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user.user_id == user_id:
            return user
    return {"error": "User not found"}

@app.post("/create_user")
def create_user(username: str, email: str):
    new_user_id = len(users) + 1
    new_user = User(user_id=new_user_id, username=username, email=email)
    users.append(new_user)
    return new_user
    