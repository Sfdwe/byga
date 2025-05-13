from typing import Any, List, Tuple, Dict, Union

def function_name(
    search: str,
    status: bool,
    *args: Any,
    **kwargs: Any
) -> Union[List[int], str]:
    """
    Обрабатывает аргументы в зависимости от параметров search и status.
    
    Параметры:
        search (str): Режим обработки ("args" или "kwargs")
        status (bool): Флаг, определяющий тип обработки
        *args: Произвольные позиционные аргументы
        **kwargs: Произвольные именованные аргументы
    
    Возвращает:
        Union[List[int], str]:
            - Если search == "args" и status == True: список целых чисел из args
            - Если search == "args" и status == False: строку из объединенных args
            - Если search == "kwargs": строку с описанием пар ключ-значение
    
    Исключения:
        ValueError: Если параметр search содержит недопустимое значение
    """
    result: List[int] = []
    result_2: str = ""
    
    if search == "args":
        if status:
            for i in args:
                if isinstance(i, int):
                    result.append(i)
            return result
        else:
            for i in args:
                result_2 += f"{i}"
            return result_2
    elif search == "kwargs":
        for k, v in kwargs.items():
            result_2 += f"Key: {k}, Value: {v}; "
        return result_2.rstrip("; ")
    else:
        raise ValueError("Invalid search parameter. Must be 'args' or 'kwargs'")
