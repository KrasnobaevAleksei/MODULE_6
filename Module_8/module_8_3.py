
class Car:
    def __init__(self, model: str, __vin : int, __numbers : str):
        self.model = model
        self.__vin = __vin
        self.__numbers = __numbers
        self.__is_valid_vin(__vin)
        self.__is_valid_number(__numbers)


    def __is_valid_vin(self, __vin):
        if not isinstance(__vin, int):
            raise Incorrect_vinNumber ("Некорректный тип vin номер")
        if __vin<1000000 or __vin>9999999:
            raise Incorrect_vinNumber ("Некорректный диапазон для vin номер")
        return True

    def __is_valid_number(self, __numbers):
        if not isinstance(__numbers, str):
            raise IncorrectCar_numbers("Некорректный тип данных для номера")
        if len(__numbers) != 6:
            raise IncorrectCar_numbers("Некорректный длина номера")
        return True
class Incorrect_vinNumber (Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCar_numbers(Exception):
    def __init__(self, message):
        self.message = message


try:
  first = Car('Model1', 1000000, 'f123dj')
except Incorrect_vinNumber as exc:
  print(exc.message)
except IncorrectCar_numbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except Incorrect_vinNumber as exc:
  print(exc.message)
except IncorrectCar_numbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')

except Incorrect_vinNumber as exc:
  print(exc.message)
except IncorrectCar_numbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')


