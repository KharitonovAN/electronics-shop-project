import codecs
import csv

class Item:
    """Класс для представления товара в магазине."""
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине."""
        self.name = name
        self.price = price
        self.quantity = quantity

        self.__name = name

        Item.all.append(self)


    def calculate_total_price(self) -> float:
        """Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара."""
        return self.price * self.quantity


    def apply_discount(self) -> None:
        """Применяет установленную скидку для конкретного товара."""
        self.price *= self.pay_rate


    @property
    def name(self):
        """Добавляем геттер для `name`, используя @property"""
        return self.__name


    @name.setter
    def name(self, name):
        """Добавляем сеттер для `name`, используя @property для проверки длины наименования
        товара не больше 10 симвовов. В противном случае, обрезать строку"""
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name


    @classmethod
    def instantiate_from_csv(cls, filename: str) -> None:
        """Класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv_"""
        cls.all.clear()
        with codecs.open(filename, 'r', encoding='utf-8', errors='replace') as file:
            data = csv.DictReader(file)
            items = []
            for d in data:
                name = d['name']
                price = float(d['price'])
                quantity = int(d['quantity'])
                item = cls(name, price, quantity)
                items.append(item)

            cls.all = items


    @staticmethod
    def string_to_number(str_number: str):
        """Cтатический метод, возвращающий число из числа-строки"""
        number = str_number.split('.')
        return int(number[0])
