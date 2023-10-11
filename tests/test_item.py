"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_calculate_total_price():
    """Тестирование метода calculate_total_price класса Item."""
    item = Item('Test', 5, 5)
    assert item.calculate_total_price() == 25


def test_apply_discount():
    """Тестирование метода apply_discount класса Item."""
    item = Item('Test', 20.0, 5)
    item.pay_rate = 0.5
    item.apply_discount()
    assert item.price == 10


def test_name_setter():
    """Проверка на изменение имени"""
    item = Item('Test', 20.0, 5)
    item.name = 'Test_1'
    assert item.name == 'Test_1'


def test_len_name():
    """Проверка длины имени не более 10 символов"""
    item = Item('Test', 20.0, 5)
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'
