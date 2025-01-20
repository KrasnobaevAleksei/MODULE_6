from fastapi import FastAPI, Path
from typing import Annotated

# запускаем из терминала python -m uvicorn module_16:app
app = FastAPI()

users = {"1": "Имя:Example, возраст: 18"}

# Возвращает БД
@app.get("/users")
async def all_users() -> dict:
    return users

# Добавляет данные пользователя
@app.post("/users/{username}/{age}")
async def add_user(username: Annotated[str, Path(min_length=3, max_length=20, description="Enter you username", example="student2025")],
                   age:Annotated[int, Path(ge=18, le=120, description="Enter you age", example="100")]) -> str:
    user_id =str(int(max(users))+1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"

# Обновление данных
@app.put("/user/{user_id}/{username}/{age}")
async def user_update(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example="99")],
                      username: Annotated[str, Path(min_length=3, max_length=20, description="Enter you username",
                                                    example="student2025")],
                      age: Annotated[int, Path(ge=18, le=120, description="Enter you age", example="100")]
                      ) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"

@app.delete("/user/{user_id}")
async def user_delete(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example="99")]):
    users.pop(str(user_id))
    return f"User {user_id} has been deleted"
