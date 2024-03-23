import pytest

from utils.main import Category, Product


@pytest.fixture
def create_category():
    category = Category("Electronics", "Electronic products")
    return category


@pytest.fixture
def create_product():
    product = Product("Phone", "Smartphone", 1000.50, 10)
    return product


def test_category_initialization(create_category):
    assert create_category.name == "Electronics"
    assert create_category.description == "Electronic products"


def test_product_initialization(create_product):
    assert create_product.name == "Phone"
    assert create_product.description == "Smartphone"
    assert create_product.price == 1000.50
    assert create_product.quantity == 10


def test_count_products(create_category, create_product):
    assert len(create_category.products) == 0
    create_category.products.append(create_product)
    assert len(create_category.products) == 1


def test_count_categories():
    assert Category.total_categories == 0
    assert Category.total_unique_products == 0
