import math

class Figure:
    sides_count = 2
    filed = True

    def __init__(self, __color, __sides: list):
        self.sides = __sides
        self.color = __color
        # if self.sides.len != self.sides_count:
        #     self.sides = 1


    def get_color(self) -> list:
        return self.color

    def set_color(self, r, g, b):
        if self.is_valid_color(r, g, b):
            self.color = []
            self.color.append(r)
            self.color.append(g)
            self.color.append(b)
        else:
            return self.color
        return self.color

    def __len__(self):
        return sum(self.sides)


    def is_valid_color(self, r, g, b):
        if 0<=r<=255 and 0<=g<=255 and 0<=b<=255:
            return True
        else:
            return False

    def is_valid_side(self, *sides):
        for i in sides:
            if isinstance(i, int) and i > 0:
                return True
            else:
                return False

    def get_sides(self) :
        return self.sides

    def set_sides(self, *new_side) -> list:
        if self.is_valid_side(*new_side) and len(new_side) == self.sides_count:
            self.sides = list(new_side)

        return self.sides


class Circle(Figure):
    sides_count = 1
    __radius = 12

    def get_square(self):
        square = math.pi * self.__radius^2
        return square

class Triangle(Figure):
    sides_count = 3
    def get_square(self):
        a = self.sides
        b = self.sides
        c = self.sides
        p=1/2*(a + b + c)
        s =  math.sqrt(p * (p - a) * (p - b) * (p - c))

        return s


class Cube(Figure):
    sides_count = 12

    def get_sides(self):
        trying =[]
        for i in range(self.sides_count):
            trying.append(self.sides)
        return trying


    def get_volume(self):
        volume = 6
        for i in range(2):
            volume *= 6
        return volume

if __name__ == "__main__":
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # # Проверка объёма (куба):
    print(cube1.get_volume())
