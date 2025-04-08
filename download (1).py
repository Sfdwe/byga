import math
import statistics

def addition(x: float, y: float) -> float:
    """Сложение двух чисел."""
    return x + y

def subtraction(x: float, y: float) -> float:
    """Вычитание двух чисел."""
    return x - y

def multiplication(x: float, y: float) -> float:
    """Умножение двух чисел."""
    return x * y

def division(x: float, y: float) -> float:
    """Деление двух чисел."""
    if y == 0:
        raise ZeroDivisionError("Деление на ноль!")
    return x / y

def exponentiation(x: float, y: float) -> float:
    """Возведение числа x в степень y."""
    return x ** y

def factorial(x: int) -> int:
    """Вычисляет факториал числа."""
    if not isinstance(x, int) or x < 0:
        raise TypeError("Факториал определен только для неотрицательных целых чисел.")
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)

def sine(x: float) -> float:
    """Вычисляет синус числа."""
    return math.sin(x)

def median(data: list) -> float:
    """Вычисляет медиану списка чисел."""
    if not data:
      raise ValueError("Список не должен быть пустым.")
    return statistics.median(data)

def calculate():
  while True:
    print("Доступные операции:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Факториал")
    print("7. Синус")
    print("8. Медиана")
    print("--------------------")

    operation = input("Операция (или 'exit'): ")

    if operation.lower() == "exit":
        break

    try:
        operation = int(operation)
        if not 1 <= operation <= 8:
            raise ValueError("Неверный номер операции.")

        if operation in (1, 2, 3, 4, 5): 