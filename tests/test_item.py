"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_calculate_total_price():
    """
    Тестирование метода calculate_total_price класса Item.
    """
    item = Item('Test', 5, 5)
    assert item.calculate_total_price() == 25


def test_apply_discount():
    """
    Тестирование метода apply_discount класса Item.
    """
    item = Item('Test', 100, 1)
    item.pay_rate = 0.9
    item.apply_discount()
    assert item.price == 9.0
