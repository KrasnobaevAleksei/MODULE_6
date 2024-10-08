class Vehicle:
    __COLOR_VARIANTS = ["blue", "red", "black"]
    def __init__(self, owner : str, __model : str, __color: str,  __engine_power: int):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return print(f"Модель: {self.__model}")

    def get_horsepower(self):
        return print(f"Мощность двигателя: {self.__engine_power}")

    def get_colorr(self):
        return print(f"Цвет: {self.__color}")

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_colorr()
        print(f"Владелец : {self.owner}")

    def set_color(self, new_color : str):
        for i in self.__COLOR_VARIANTS:
            if i.lower() ==new_color.lower() :
                self.__color = new_color
                return self.__color

        print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()



