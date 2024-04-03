from abc import ABC, abstractmethod


class Category:
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.total_categories += 1
        Category.total_unique_products += len(products)

    # def __len__(self):
    # return len(self.__products)

    # def __str__(self):
    # return f"{self.name},количество продуктов: {self.__products} шт."

    def add_product(self, __product):
        self.__products.append(__product)

    # def __add__(self, other):
    # if not isinstance(other, Category):
    # raise ValueError

    @property
    def products(self):
        str_products = []
        for i in self.__products:
            str_products.append(f"{i.name}, {i.price} руб. Остаток:{i.quantity} шт.")
        return "\n".join(str_products)


class Product:
    def __init__(self, name, description, _price, quantity):
        self.name = name
        self.description = description
        self._price = _price
        self.quantity = quantity

    # def __len__(self):
    # return len(self.quantity)

    # @abstractmethod
    # def __str__(self):
    # return f"{self.name},{self.price}руб. Остаток:{self.quantity} шт."

    # def __add__(self, other):
    # classes = [Category, Product, Smartphone, Grass]
    # for i in classes:
    # if issubclass(i.__class__,  # какой класс использовать):
    # raise ValueError
    # else:
    # return self.price * self.quantity + other.price * self.quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("введите корректное значение")
        self._price = value

    @classmethod
    def create_product(cls, **kwargs):
        return cls(**kwargs)

# class Smartphone(Product):
# ef __init__(self, name, description, price, quantity, efficiency, model, ram, color):
# super().__init__(name, description, price, quantity)
# self.efficiency = efficiency
# self.model = model
# self.ram = ram
# self.color = color

# def __str__(self):
# return f"{self.name},{self.price}руб. Остаток:{self.quantity} шт."


# class Grass(Product):
# def __init__(self, name, description, price, quantity, made, grow, color):
# super().__init__(name, description, price, quantity)
# self.made = made
# self.grow = grow
# self.color = color

# def __str__(self):
# return f"{self.name},{self.price}руб. Остаток:{self.quantity} шт."


# class MixinLog:
# def __repr__(self):
# return f"{self.Category}('{self.name}', '{self.description}', {self.__products})"  # какие атрибуты надо написать
