from fastapi import FastAPI, Request,Path
from typing import Annotated
from pydantic import BaseModel
from typing import List
from fastapi import HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

class User(BaseModel):
    id: int 
    username : str
    age : int

users = []

@app.get("/")
async def get_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.get("/user/{user_id}")
async def read_user(request: Request, user_id: int = Path(ge=1, le=100, title="User ID from 1 to 100", description="Enter User ID",example="1"))-> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "user": users[user_id-1]})
    raise HTTPException(status_code=404, detail=f"User ID {user_id} не найден")

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