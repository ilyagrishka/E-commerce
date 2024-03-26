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

    def get_products(self):
        return self.__products


class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @property
    def get_price(self):
        return self.price

    @classmethod
    def create_product(cls, name, description, price, quantity):
        return cls(name, description, price, quantity)
