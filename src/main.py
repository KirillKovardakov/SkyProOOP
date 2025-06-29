from typing import Optional


class Product:
    """Класс для определения продуктов"""

    name: str
    description: str
    __price: float = 0.0
    quantity: int = 0

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Конструктор класса"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}, {self.__price} руб. Остаток:{self.quantity} шт.'

    def __add__(self, other):
        """Возвращает сумму стоимости (цена * количество) двух продуктов"""
        return self.__price * self.quantity + other.__price * other.quantity

    @classmethod
    def new_product(cls, product_data: dict, category=None):
        """
        Создает новый продукт или обновляет существующий в переданной категории.
        """
        if category is None:
            category = []
        name = product_data.get("name")
        description = product_data.get("description", "")
        price = product_data.get("price", 0.0)
        quantity = product_data.get("quantity", 0)

        for existing_product in category.get_product_list():
            if existing_product.name == name:
                # Обновляем существующий продукт
                existing_product.quantity += quantity
                existing_product.price = max(existing_product.price, price)
                return existing_product

        # Если товара не было — создаём и добавляем в категорию
        new_prod = cls(name, description, price, quantity)
        category.add_product(new_prod)
        return new_prod

    @property
    def price(self):
        """Возвращает цену"""
        return self.__price

    @price.setter
    def price(self, new_price: float):
        """Проверяет на снижение цены продукта и устанавливает новую"""
        if new_price > 0:
            if self.price > new_price:
                user_confirm_price_reduction = input("\nConfirm the price reduction (y/n)\n") == 'y'
                if user_confirm_price_reduction:
                    self.__price = new_price
            else:
                self.__price = new_price
        else:
            print('Цена не должна быть нулевая или отрицательная')


class Category:
    __name: str
    __description: str
    __products: list
    category_count: int = 0
    product_count: int = 0
    """Класс для определения категорий продуктов"""

    def __init__(self, name: str, description: str, products: Optional[list[Product]] = None):
        """Конструктор класса Category"""
        self.__name = name
        self.__description = description
        self.__products = products or []
        self.category_count += 1
        self.product_count += len(products)

    def __str__(self):
        all_product_count_in_category = sum([product.quantity for product in self.__products])
        return f'{self.__name}, количество продуктов: {all_product_count_in_category} шт.'

    def add_product(self, new_product_of_category: Optional[Product]):
        """Добавляет продукт к категории"""
        self.__products.append(new_product_of_category)
        self.product_count += 1

    @property
    def products(self) -> list:
        """Возвращает Список продуктов list[Формат f строки]"""
        result = [str(product) for product in self.__products]
        return result

    def get_product_list(self):
        """Возвращает простой список продуктов list"""
        return self.__products


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(str(category1))

    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)