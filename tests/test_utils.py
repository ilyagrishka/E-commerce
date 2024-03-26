import pytest

from utils.main import Category, Product


@pytest.fixture
def create_category():
    category = Category("Electronics", "Electronic products", [Product("Phone", "Smartphone", 1000.50, 10),
                                                               Product("laptops", "electronic", 2000, 10)])

    return category


@pytest.fixture
def create_product():
    product = Product("Phone", "Smartphone", 1000.50, 10)
    return product


@pytest.fixture
def list_products():
    products = [
        Product("Phone", "Smartphone", 1000.50, 10),
        Product("laptops", "electronic", 2000, 10)
    ]
    return products


def test_category_initialization(create_category):
    assert create_category.name == "Electronics"
    assert create_category.description == "Electronic products"


def test_product_initialization(create_product):
    assert create_product.name == "Phone"
    assert create_product.description == "Smartphone"
    assert create_product.price == 1000.50
    assert create_product.quantity == 10


def test_count_products(create_category, list_products, create_product):
    assert len(create_category.get_products()) == len(list_products)
    create_category.add_product(create_product)
    l_list = list_products.copy()
    l_list.append(create_product)
    assert len(create_category.get_products()) == len(l_list)


def test_count_categories():
    assert Category.total_categories == 2
    assert Category.total_unique_products == 4
