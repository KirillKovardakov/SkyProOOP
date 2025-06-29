import pytest
from src.main import Product, Category


@pytest.fixture
def fixture_product():
    """Фикстура которая возвращает объект класса Product"""
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def fixture_category():
    """Фикстура которая возвращает объект класса Category"""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )


def test_product(fixture_product):
    """тестируем класс Product"""
    product1 = fixture_product
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5


def test_new_product(fixture_product, fixture_category):
    category1 = fixture_category
    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 15}, category1)
    assert new_product.name == 'Samsung Galaxy S23 Ultra'
    assert new_product.description == '256GB, Серый цвет, 200MP камера'
    assert new_product.price == 180000.0
    assert new_product.quantity == 20

    new_product = Product.new_product(
        {"name": "Samsung Galaxy S230 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 380000.0,
         "quantity": 1}, category1)
    assert new_product.name == 'Samsung Galaxy S230 Ultra'
    assert new_product.description == '256GB, Серый цвет, 200MP камера'
    assert new_product.price == 380000.0
    assert new_product.quantity == 1


def test_product_mystical_methods(fixture_product):
    product1 = fixture_product
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    assert str(product1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток:5 шт."
    assert product1 + product2 == 2580000.0


def test_category(fixture_category):
    """тестируем класс Category"""
    category = fixture_category
    assert category.products == ['Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток:5 шт.',
                                 'Iphone 15, 210000.0 руб. Остаток:8 шт.',
                                 'Xiaomi Redmi Note 11, 31000.0 руб. Остаток:14 шт.']
    assert category.category_count == 1
    assert category.product_count == 3
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category.add_product(product4)
    assert category.products == ['Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток:5 шт.',
                                 'Iphone 15, 210000.0 руб. Остаток:8 шт.',
                                 'Xiaomi Redmi Note 11, 31000.0 руб. Остаток:14 шт.',
                                 '55" QLED 4K, 123000.0 руб. Остаток:7 шт.']
    assert str(category) == "Смартфоны, количество продуктов: 34 шт."
