import pytest
from src.main import Product, Category


@pytest.fixture
def fixture_product_apple():
    """Фикстура которая возвращает объект класса Product"""
    return Product("apple", "desc1", 5, 10)


@pytest.fixture
def fixture_category():
    """Фикстура которая возвращает объект класса Category"""
    pr1 = Product("яблоко", "desc1", 5, 10)
    pr2 = Product("grusha", "desc1", 4, 15)
    pr3 = Product("apelsin", "desc1", 6, 6)
    return Category("fruits", "test_fruits", [pr1, pr2, pr3])


def test_product(fixture_product_apple):
    """тестируем класс Product"""
    assert fixture_product_apple.name == "apple"
    assert fixture_product_apple.description == "desc1"
    assert fixture_product_apple.price == 5
    assert fixture_product_apple.quantity == 10


def test_category(fixture_category):
    """тестируем класс Category"""
    assert fixture_category.name == "fruits"
    assert fixture_category.description == "test_fruits"
    assert fixture_category.count_category == 1
    assert fixture_category.count_products == 3
