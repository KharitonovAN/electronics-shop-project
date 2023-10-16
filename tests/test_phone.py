"""тесты с использованием pytest для модуля phone."""
from src.phone import Phone


def test_phone():
    """Проверка вывода всех данных"""
    phone = Phone("test1", 2000, 2, 2)
    assert phone.name == "test1"
    assert phone.price == 2000
    assert phone.quantity == 2
    assert phone.number_of_sim == 2


def test_number_of_sim_setter():
    """Проверка количества сим-карт"""
    phone = Phone("test1", 2000, 2, 2)
    phone.number_of_sim = 2
    assert phone.number_of_sim == 2

