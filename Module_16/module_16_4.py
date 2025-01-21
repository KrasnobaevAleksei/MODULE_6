from fastapi import FastAPI, status, Body, HTTPException, Path
from typing import Annotated
from typing import List
from pydantic import BaseModel
# запускаем из терминала python -m uvicorn module_16:app
app = FastAPI()

users = []

class User(BaseModel):
    id:int
    username:str
    age:int
# Выводит список всех пользователей
@app.get("/users")
def get_all_users():
    return users

# Добавляет объект User в список
@app.post("/user/{username}/{age}")
def add_user(user: User):
    new_id = max((t.id for t in users), default=0)+1
    new_user=User(id=new_id, username=user.username, age=user.age)
    users.append(new_user)
    return new_user
#Обновляет данные юзера
@app.put("/user/{user_id}/{username}/{age}")
def update_user(user:User, user_id:int):
        for t in users:
            if t.id == user_id:
                t.username = user.username
                t.age = user.age
                return t
        raise HTTPException(status_code=404, detail="Message not found")

@app.delete("/user/{user_id}")
def delete_user(user_id:int):
        for i, t in enumerate(users):
            if t.id == user_id:
                del users[i]
                return "Запись удалена"
        raise HTTPException(status_code=404, detail="Message not found")