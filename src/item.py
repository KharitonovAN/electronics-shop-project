import csv


class InstantiateCSVError(Exception):
    """Класс исключения для ошибок при инициализации из CSV"""
    def __init__(self, message):
        super().__init__(message)


class Item:
    """Класс для представления товара в магазине."""
    pay_rate = 1.0
    all = []
    data = []

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
    def instantiate_from_csv(cls, filename: str = '../src/items.csv'):
        """Класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv_"""
        try:
            with open(filename, 'r', newline='') as file:
                data = csv.DictReader(file)
                items = []
                for data_ in data:
                    try:
                        name = data_['name']
                        price = float(data_['price'])
                        quantity = int(data_['quantity'])
                    except KeyError:
                        raise InstantiateCSVError("Файл item.csv поврежден: отсутствует одна из колонок данных")
                    item = cls(name, price, quantity)
                    items.append(item)

                cls.all = items
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")


    @staticmethod
    def string_to_number(str_number: str):
        """Cтатический метод, возвращающий число из числа-строки"""
        number = str_number.split('.')
        return int(number[0])

    def __repr__(self):
        """Отображает информацию в режиме отладки"""
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """Отображает информацию в режиме для пользователя"""
        return self.__name

    def __add__(self, other):
        """Сложение количества товаров из классов Item и Phone"""
        if isinstance(other, Item):
            return self.quantity + other.quantity
