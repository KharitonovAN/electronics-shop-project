"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item, InstantiateCSVError


def test_name_setter():
    """Проверка на изменение имени"""
    item = Item('Test', 20.0, 5)
    item.name = 'Test_1'
    assert item.name == 'Test_1'


def test_name():
    """Проверка на длину названия, не более 10 символов"""
    item = Item('Test', 20, 5)
    item.name = 'СуперСмартфон'
    assert item.name == 'СуперСмарт'


def test__repr__():
    """Тест метода __repr__"""
    item = Item('Test', 20, 5)
    assert repr(item) == "Item('Test', 20, 5)"


def test__str__():
    """Тест метода __str__"""
    item = Item('Test', 20, 5)
    assert str(item) == 'Test'


def test__init__():
    """Тестирование __init__"""
    item = Item('Test', 20, 5)
    assert item.name == 'Test'
    assert item.price == 20
    assert item.quantity == 5


def test_string_to_number():
    """Тест на функцию создания экземпляров"""
    assert Item.string_to_number('5') == 5


def setup_class(self):
    """Установка начального состояния перед выполнением тестов"""
    self.item = Item("Test Item", 10.0, 5)


def test_init(self):
    """Проверяет инициализацию экземпляра Item"""
    assert self.item.name == "Test Item"
    assert self.item.price == 10.0
    assert self.item.quantity == 5


def test_string_conversion(self):
    """Проверяет строковое представление экземпляра Item"""
    assert str(self.item) == "Test Item"
    assert repr(self.item) == "Item('Test Item', 10.0, 5)"


def test_add_items(self):
    """Проверяет оператор сложения экземпляров Item"""
    new_item = Item("Another Item", 5.0, 3)
    combined_item = self.item + new_item
    assert combined_item.quantity == 8


def test_instantiate_from_csv_with_nonexistent_file():
    """Проверяет исключение при попытке загрузить несуществующий CSV-файл"""
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv("nonexistent.csv")


def test_name_property(self):
    """Проверяет ограничение на длину свойства name"""
    self.item.name = "A Very Long Name for an Item with More Than 20 Characters"
    assert len(self.item.name) == 10  # Убедимся, что ограничение на 10 символов работает


def test_calculate_total_price(self):
    """Проверяет расчет общей стоимости товара."""
    assert self.item.calculate_total_price() == 50.0


def test_apply_discount(self):
    """Проверяет применение скидки к товару."""
    self.item.apply_discount()
    assert self.item.price == 10.0 * Item.pay_rate


# Тесты для класса InstantiateCSVError
class TestInstantiateCSVError:
    """
    Тесты для класса InstantiateCSVError.
    """
    def test_init(self):
        """
        Проверяет инициализацию экземпляра InstantiateCSVError.
        """
        error = InstantiateCSVError("Test error message")
        assert str(error) == "Test error message"
