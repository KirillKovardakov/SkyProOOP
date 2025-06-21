class Product:
    """Класс для определения продуктов"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    name: str
    description: str
    products: list
    count_category: int = 0
    count_products: int = 0
    """Класс для определения категорий продуктов"""

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.products = products
        self.count_category += 1
        self.count_products += len(products)
