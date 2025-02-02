from fastapi import FastAPI
from routers import task
from routers import user

app=FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(user.router)
app.include_router(task.router)

#from sqlalchemy.schema import CreateTable
#from models import *

#print(CreateTable(Task.__table__))
#print(CreateTable(User.__table__))