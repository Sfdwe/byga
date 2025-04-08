from typing import List, Union

def multiply_list(data: List[Union[int, float]], multiplier: Union[int, float] = 2) -> List[Union[int, float]]:
    """Умножает каждый элемент списка на заданный множитель.

    Args:
        data: Список чисел.
        multiplier: Множитель. По умолчанию равен 2.

    Returns:
        Новый список с умноженными элементами.
    """
    return [item * multiplier for item in data]


def multiply_list_lambda(data: List[Union[int, float]], multiplier: Union[int, float] = 2) -> List[Union[int, float]]:
    """Умножает каждый элемент списка на заданный множитель (лямбда-функция).

    Args:
        data: Список чисел.
        multiplier: Множитель. По умолчанию равен 2.

    Returns:
        Новый список с умноженными элементами.
    """
    return list(map(lambda x: x * multiplier, data))


