class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor
    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floor:
            for i in range(new_floor):
                print(i+1)
        else:
            print("Такого этажа не существует в этом доме")
    # метод eq
    def __eq__(self, other):
        if isinstance(other, int) or isinstance(other, House):
            return self.number_of_floor == other
    # метод ne
    def __ne__(self, other):
        if isinstance(other, int) or isinstance(other, House):
            return self.number_of_floor == other
    # метод lt
    def __lt__(self, other):
        if isinstance(other, int) or isinstance(other, House):
            return self.number_of_floor < other
    # метод le
    def __le__(self, other):
        if isinstance(other, int) or isinstance(other, House):
            return self.number_of_floor <= other
    # метод gt
    def __gt__(self, other):
        if isinstance(other, int) or isinstance(other, House):
            return self.number_of_floor > other
    # метод ge
    def __ge__(self, other):
        if isinstance(other, int) or isinstance(other, House):
            return self.number_of_floor >= other
    # метод __add__
    def __add__(self, other):
        self.number_of_floor += other
        return self

    def __iadd__(self, other):
        return self.__add__(other)
        # self.number_of_floor += other
        # return self
    # def __iadd__(self, other1):
    #      self.__add__(self, other1)

    def __radd__(self, other):
        return self.__add__(other)
        # self.number_of_floor += other
        # return self

    # метод len
    def __len__(self):
        return self.number_of_floor

    #метод str
    def __str__(self):
        return f"Название: {self.name}, количество этажей: {self.number_of_floor}"


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
