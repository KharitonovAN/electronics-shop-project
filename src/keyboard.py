from src.item import Item


class MixinLang:
    """Класс-миксин по изменению раскладки клавиатуры"""
    def __init__(self):
        """Инициализация класс-миксина keyboard
        language: Язык раскладки
        По умолчанию 'EN'"""
        self.__language = 'EN'

    def change_lang(self):
        """Функция для изменения языка (раскладки клавиатуры).
        Всего поддерживается два языка: `EN` и `RU`"""
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'

    def save_lang(self):
        """Функция для хранения раскладки клавиатуры"""
        return self.__language


class Keyboard(Item, MixinLang):
    """Класс `Keyboard` для товара 'клавиатура'"""
    def __init__(self, name: str, price: float, quantity: int) -> None:
        """Инициализация класса `Keyboard` наследуемый от 'Item' и с 'подмешиванием' из 'MixinLang'"""
        super().__init__(name, price, quantity)
        MixinLang.__init__(self)
