from fastapi import FastAPI, Path
from typing import Annotated
from fastapi import HTTPException

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def get_users():
    return users

@app.post("/user/{username}/{age}")
async def set_user(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username",example="UrbanUser")],
                    age: Annotated[int, Path(ge=18, le=120, title="User age from 18 to 120", description="Enter age",example="24")]):
    new_id = len(users)+1
    users[str(new_id)]=f"Имя: {username}, возраст: {age}"
    return f"User {new_id} is registered."

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int,Path(ge=1, title="User ID", description="Enter User ID",example="1")],
                    username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username",example="UrbanUser")],
                    age: Annotated[int, Path(ge=18, le=120, title="User age from 18 to 120", description="Enter age",example="24")]):
    for key, value in users.items():
        if str(user_id) == key:
            users[key]=f"Имя: {username}, возраст: {age}"
            return f"The user {user_id} is updated"
    raise HTTPException(status_code=404, detail=f"User ID {user_id} не найден")

@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int,Path(ge=1, title="User ID", description="Enter User ID",example="1")]):
    for key, value in users.items():
        if str(user_id) == key:
            del users[key]
            return f"User {user_id} has been deleted"
    raise HTTPException(status_code=404, detail=f"User ID {user_id} не найден")