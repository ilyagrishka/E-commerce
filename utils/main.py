from abc import ABC, abstractmethod


class MixinLog:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self)

    def __repr__(self):
        a = str(self.__dict__).replace('{', '').replace('}', '')
        return f'{self.__class__.__name__} {a}'


class Category:
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.total_categories += 1
        Category.total_unique_products += len(products)

    def __len__(self):
        return len(self.__products)

    def __str__(self):
        return f"{self.name},количество продуктов:{len(self)} шт."

    def add_product(self, product):
        if not isinstance(product, Category):
            raise ValueError
        self.__products.append(product)

    @property
    def products(self):
        str_products = []
        for i in self.__products:
            str_products.append(f"{i.name}, {i.price} руб. Остаток:{i.quantity} шт.")
        return "\n".join(str_products)
class Product(ABC):
    def __init__(self, name, description, _price, quantity):
        self.name = name
        self.description = description
        self._price = _price
        self.quantity = quantity

    def __len__(self):
        return self.quantity

    @abstractmethod
    def __str__(self):
        return f"{self.name},{self.price}руб. Остаток:{self.quantity} шт."

    def __add__(self, other):
        if not type(other) == self.__class__:
            raise TypeError
        return self.price * self.quantity + other.price * other.quantity

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


class Smartphone(MixinLog, Product):
    def __init__(self, name, description, price, quantity, efficiency, model, ram, color):

        self.efficiency = efficiency
        self.model = model
        self.ram = ram
        self.color = color
        super().__init__(name, description, price, quantity)

    def __str__(self):
        return f"{self.name},{self.price}руб. Остаток:{self.quantity} шт."


class Grass(MixinLog, Product):
    def __init__(self, name, description, price, quantity, made, grow, color):

        self.made = made
        self.grow = grow
        self.color = color
        super().__init__(name, description, price, quantity)

    def __str__(self):
        return f"{self.name},{self.price}руб. Остаток:{self.quantity} шт."
