from fastapi import FastAPI

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
async def user_page(user_id: int):
    return (f"Вы вошли как пользователь № {user_id}")

# Когда в адресной строке набираешь(вводишь запрос) "/user?username = Alex& age = 12",
# в главном окне выводится надпись из return с Alex 12
@app.get("/user")
async def user_data(username : str, age: int):
    return (f"Информация о пользователе. Имя : {username}, Возраст : {age}")

