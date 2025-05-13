from typing import List, TypeVar, Union

T = TypeVar('T', int, float, str)

def multiply_list_elements(elements: List[T], multiplier: Union[int, float] = 2) -> List[T]:
    """Умножает каждый элемент списка на множитель."""
    return [element * multiplier for element in elements]

if __name__ == "__main__":
    # Ввод данных от пользователя
    input_list = input("Введите список чисел через пробел: ").split()
    multiplier_input = input("Введите множитель (по умолчанию 2): ")
    
    # Преобразование ввода
    try:
        elements = [int(x) if x.isdigit() else float(x) for x in input_list]
    except ValueError:
        elements = input_list  # если не числа, оставляем как строки
    
    multiplier = float(multiplier_input) if multiplier_input else 2
    if multiplier.is_integer():
        multiplier = int(multiplier)
    
    # Вызов функции
    result_func = multiply_list_elements(elements, multiplier)
    print(f"Результат (функция): {result_func}")
    
    # Лямбда-функция с map
    lambda_result = list(map(lambda x: x * multiplier, elements))
    print(f"Результат (лямбда-функция): {lambda_result}")
