from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return "Главная страница"

@app.get("/user/admin")
async def admin():
    return "Вы вошли как администратор"
    
@app.get("/user/{user_id}")
async def read_user(user_id: int):
    return f"Вы вошли как пользователь № {user_id}"

@app.get("/user")
async def info_user(username: str, age: int):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"