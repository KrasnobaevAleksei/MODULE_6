class Product:
    def __init__(self, name: str, weight : float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        result = self.name + ", " + str(self.weight) + ", " +  self.category
        return result

class Shop:
    __file_name = "product.txt"
    def get_products(self):
        open_ = open(self.__file_name, "r")
        all_products = open_.read()
        open_.close()
        return all_products

    def add(self, *products):
        open_ = open(self.__file_name, "a")
        for i in products:
            if i.name in self.get_products():
                print(f"Продукт {i} уже есть в магазине")
            else:
                open_.write(str(i) + "\n")
        open_.close()

if __name__ == "__main__":
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2) # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())
