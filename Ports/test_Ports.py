import pytest
from NetworkCardSpeed01 import NetworkCardSpeed01
from NetworkCardSpeed02 import NetworkCardSpeed02
from NetworkCardSpeed03 import NetworkCardSpeed03
from NetworkCardSpeed04 import NetworkCardSpeed04
from NetworkCardSpeed05 import NetworkCardSpeed05
from NetworkCardSpeed06 import NetworkCardSpeed06
from NetworkCardSpeed07 import NetworkCardSpeed07
from NetworkCardSpeed08 import NetworkCardSpeed08
from NetworkCardSpeed09 import NetworkCardSpeed09
from NetworkCardSpeed010 import NetworkCardSpeed010

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

    # Перевіряємо, чи метод test_data існує
    assert hasattr(instance, "test_data"), f"{card_class.__name__} має мати метод test_data"

    # Викликаємо test_data і перевіряємо, чи дані коректні
    data = instance.test_data()
    assert isinstance(data, list), f"{card_class.__name__}.test_data має повертати список"
    for item in data:
        assert isinstance(item, tuple), f"{card_class.__name__}.test_data має містити кортежі"
        assert len(item) == 2, f"{card_class.__name__}.test_data має містити кортежі з двома елементами"
        assert isinstance(item[1], list), f"Другий елемент кортежу в {card_class.__name__}.test_data має бути списком"
