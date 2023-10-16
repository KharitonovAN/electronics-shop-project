from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        """Класс Phone.
        name: Название товара.
        price: Цена за единицу смартфона.
        quantity: Количество смартфонов в магазине.
        number_of_sim: Количество поддерживаемых сим-карт."""
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        """Отображает информацию в режиме отладки"""
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        """Отображает информацию в режиме для пользователя"""
        return self.name

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, quantity_sim):
        """Сеттер содержащий количество поддерживаемых сим-карт"""
        self.__number_of_sim = quantity_sim


