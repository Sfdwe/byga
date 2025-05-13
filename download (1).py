import math
from statistics import median
from typing import List, Union

Number = Union[int, float]

def check_number(value: str) -> Number:
    """Проверяет и преобразует строку в число (int или float)."""
    try:
        return int(value) if value.isdigit() else float(value)
    except ValueError:
        raise ValueError("Ошибка: введено не число")

def addition(a: Number, b: Number) -> Number:
    """Сложение двух чисел."""
    if not (isinstance(a, (int, float)) or not (isinstance(b, (int, float))):
        raise TypeError("Ошибка: оба аргумента должны быть числами")
    return a + b

def subtraction(a: Number, b: Number) -> Number:
    """Вычитание двух чисел."""
    if not (isinstance(a, (int, float)) or not (isinstance(b, (int, float)))):
        raise TypeError("Ошибка: оба аргумента должны быть числами")
    return a - b

def multiplication(a: Number, b: Number) -> Number:
    """Умножение двух чисел."""
    if not (isinstance(a, (int, float)) or not (isinstance(b, (int, float)))):
        raise TypeError("Ошибка: оба аргумента должны быть числами")
    return a * b

def division(a: Number, b: Number, div_type: str = '/') -> Number:
    """Деление с выбором типа: обычное, целочисленное или остаток."""
    if not (isinstance(a, (int, float)) or not (isinstance(b, (int, float))):
        raise TypeError("Ошибка: оба аргумента должны быть числами")
    if b == 0:
        raise ZeroDivisionError("Ошибка: деление на ноль невозможно")
    
    if div_type == '//':
        return a // b
    elif div_type == '%':
        return a % b
    else:
        return a / b

def power(a: Number, b: Number) -> Number:
    """Возведение в степень."""
    if not (isinstance(a, (int, float)) or not (isinstance(b, (int, float))):
        raise TypeError("Ошибка: оба аргумента должны быть числами")
    return a ** b

def factorial(n: int) -> int:
    """Факториал числа."""
    if not isinstance(n, int):
        raise TypeError("Ошибка: аргумент должен быть целым числом")
    if n < 0:
        raise ValueError("Ошибка: факториал отрицательного числа не определен")
    return math.factorial(n)

def sin(x: Number) -> float:
    """Синус числа (в радианах)."""
    if not isinstance(x, (int, float)):
        raise TypeError("Ошибка: аргумент должен быть числом")
    return math.sin(x)

def calculate_median(numbers: List[Number]) -> float:
    """Медиана списка чисел."""
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("Ошибка: все элементы списка должны быть числами")
    if not numbers:
        raise ValueError("Ошибка: список чисел не может быть пустым")
    return median(numbers)

def print_operations():
    """Выводит список доступных операций."""
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

def main():
    print_operations()
    
    while True:
        operation = input("Операция: ").strip().lower()
        
        if operation in ('exit', 'quit', 'q'):
            print("Завершение работы калькулятора")
            break
        
        try:
            if operation == '1':
                a = check_number(input("Слагаемое 1: "))
                b = check_number(input("Слагаемое 2: "))
                print(f">>> {addition(a, b)}")
            
            elif operation == '2':
                a = check_number(input("Уменьшаемое: "))
                b = check_number(input("Вычитаемое: "))
                print(f">>> {subtraction(a, b)}")
            
            elif operation == '3':
                a = check_number(input("Множитель 1: "))
                b = check_number(input("Множитель 2: "))
                print(f">>> {multiplication(a, b)}")
            
            elif operation == '4':
                a = check_number(input("Делимое: "))
                b = check_number(input("Делитель: "))
                div_type = input("Тип деления (/, //, %): ").strip()
                print(f">>> {division(a, b, div_type)}")
            
            elif operation == '5':
                a = check_number(input("Основание: "))
                b = check_number(input("Степень: "))
                print(f">>> {power(a, b)}")
            
            elif operation == '6':
                n = check_number(input("Число: "))
                if not isinstance(n, int):
                    raise TypeError("Факториал вычисляется только для целых чисел")
                print(f">>> {factorial(n)}")
            
            elif operation == '7':
                x = check_number(input("Число (в радианах): "))
                print(f">>> {sin(x)}")
            
            elif operation == '8':
                numbers = [check_number(x) for x in input("Список чисел: ").split()]
                print(f">>> {calculate_median(numbers)}")
            
            else:
                print("Неизвестная операция. Попробуйте снова.")
        
        except Exception as e:
            print(f"Ошибка: {e}")
        
        print("--------------------")

if __name__ == "__main__":
    main()
