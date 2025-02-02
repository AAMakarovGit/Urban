from fastapi import FastAPI
from typing import Annotated
from pydantic import BaseModel
from typing import List
from fastapi import HTTPException

app = FastAPI()

class User(BaseModel):
    id: int 
    username : str
    age : int

users = []

@app.get("/users")
async def get_users() -> List[User]:
    return users

@app.post("/user/{username}/{age}")
async def set_user(username: str, age: int) -> str:
    us=User(id=len(users)+1,username=username,age=age)
    users.append(us)
    return f"User {us.id} is registered."

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str, age: int) -> str:
    for user in users:
        if user.id== user_id:
            user.username=username
            user.age=age
            return f"The user {user_id} is updated"
    raise HTTPException(status_code=404, detail=f"User ID {user_id} не найден")

@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> str:
    for user in users:
        if user.id== user_id:
            users.remove(user)
            return f"User {user_id} has been deleted"
    raise HTTPException(status_code=404, detail=f"User ID {user_id} не найден")