class Category:
    total_categories = 0
    total_unique_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.total_categories += 1
        Category.total_unique_products += len(products)

    def add_product(self, product):
        self.__products.append(product)

    @property
    def get_products(self):
        list_products = []
        for i in self.__products:
            list_products.append(f"{i.name}, {i.price} руб. Остаток:{i.quantity} шт.")
        return list_products


class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value:
            self._price = value
        else:
            print("введите корректное значение")

    @classmethod
    def create_product(cls, **kwargs):
        return cls(**kwargs)
