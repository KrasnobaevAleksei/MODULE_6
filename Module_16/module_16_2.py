from fastapi import FastAPI, Path
from typing import Annotated

# запускаем из терминала python -m uvicorn module_16:app
app = FastAPI()

# Когда в адресной строке набираешь(вводишь запрос) прямой слеш, в главном окне выводится надпись из return
@app.get("/")
async def main_page():
    return ("Главная страница")

# Когда в адресной строке набираешь(вводишь запрос) "/user/admin", в главном окне выводится надпись из return
@app.get("/user/admin")
async def admin_page():
    return ("Вы вошли как администратор")

# Когда в адресной строке набираешь(вводишь запрос) "/user/123",
# в главном окне выводится надпись из return с переменной {user_id}
@app.get("/user/{user_id}")
async def user_page(user_id: Annotated[int, Path(ge=1, le=100, discription="Enter User ID", example="99")]):
    return (f"Вы вошли как пользователь № {user_id}")

# Когда в адресной строке набираешь(вводишь запрос) "/user?username = Alex& age = 12",
# в главном окне выводится надпись из return с Alex 12
@app.get("/user/{username}/{age}")
async def user_data(username: Annotated[str, Path(min_length=5, max_length=20, discription="Enter username", example="UrbanUser" )]
                    , age: Annotated[int, Path(ge=18, le=120, discription="Enter age", example="24")]):
    return (f"Информация о пользователе. Имя : {username}, Возраст : {age}")
