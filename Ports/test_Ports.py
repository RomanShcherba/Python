import pytest
import NetworkCardSpeed01
import NetworkCardSpeed02
import NetworkCardSpeed03
import NetworkCardSpeed04
import NetworkCardSpeed05
import NetworkCardSpeed06
import NetworkCardSpeed07
import NetworkCardSpeed08
import NetworkCardSpeed09
import NetworkCardSpeed010

# Список класів для тестування
card_classes = [
    NetworkCardSpeed01,
    NetworkCardSpeed02,
    NetworkCardSpeed03,
    NetworkCardSpeed04,
    NetworkCardSpeed05,
    NetworkCardSpeed06,
    NetworkCardSpeed07,
    NetworkCardSpeed08,
    NetworkCardSpeed09,
    NetworkCardSpeed010,
]

@pytest.mark.parametrize("card_class", card_classes)
def test_card_class(card_class):
    """Тест для перевірки класів NetworkCardSpeed"""
    instance = card_class()

    # Перевіряємо наявність обов'язкових атрибутів
    assert hasattr(card_class, "NAME"), f"{card_class.__name__} має мати атрибут NAME"
    assert hasattr(card_class, "DESCRIPTION"), f"{card_class.__name__} має мати атрибут DESCRIPTION"

    # Перевіряємо, чи метод test_data існує і повертає дані
    assert hasattr(instance, "test_data"), f"{card_class.__name__} має мати метод test_data"
    data = instance.test_data()
    assert isinstance(data, list), f"{card_class.__name__}.test_data має повертати список"
    assert all(isinstance(item, tuple) for item in data), f"{card_class.__name__}.test_data має містити кортежі"
