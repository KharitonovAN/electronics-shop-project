from src.item import Item


class MixinLang:
    """Класс-миксин по изменению раскладки клавиатуры"""
    def __init__(self):
        """Инициализация класс-миксина keyboard
        language: Язык раскладки
        По умолчанию 'EN'"""
        language = 'EN'
        self.language = language

    def change_lang(self):
        """Функция для изменения языка (раскладки клавиатуры).
        Всего поддерживается два языка: `EN` и `RU`"""
        if self.language == 'EN':
            self.language = 'RU'
        else:
            self.language = 'EN'

    def save_lang(self):
        """Функция для хранения раскладки клавиатуры"""
        print(f'Язык раскладки клавиатуры - {self.language}')


class Keyboard(Item, MixinLang):
    """Класс `Keyboard` для товара 'клавиатура'"""
    def __init__(self, name: str, price: float, quantity: int, languange='EN'):
        """Инициализация класса `Keyboard` наследуемый от 'Item' и с 'подмешиванием' из 'MixinLang'"""
        super().__init__(name, price, quantity)
        self.language = languange
        if self.language.upper() != 'EN' and self.language.upper() != 'RU':
            raise ValueError('Всего поддерживается два языка: `EN` и `RU`')
