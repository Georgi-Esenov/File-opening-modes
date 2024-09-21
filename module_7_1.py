from pprint import pprint


class Shop:

    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        a = file.read()
        file.close()
        return a

    def add(self, *products):
        file = open(self.__file_name, 'r+')
        for i in products:
            if str(i) in self.get_products():
                print(f"Продукт {str(i)} уже есть в магазине")
            else:
                file.write(str(i)+'\n')
        file.close()


class Product(Shop):
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category} "


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
