from typing import List, Union

def function_name(search: str, status: bool, *args: Union[int, str], **kwargs: str) -> Union[List[int], str]:
    """Обрабатывает аргументы в зависимости от параметров search и status.

    Args:
        search: Если 'args', обрабатывает аргументы *args. 
                 Если 'kwargs', обрабатывает аргументы **kwargs.
        status: Определяет режим обработки *args (если search == 'args').
                Если True, возвращает список целых чисел из *args.
                Если False, возвращает строку, объединяющую все элементы *args.
        *args: Произвольное количество позиционных аргументов.
        **kwargs: Произвольное количество именованных аргументов.

    Returns:
        Список целых чисел (если search == 'args' and status == True), 
        строку (если search == 'args' and status == False или search == 'kwargs'),
        либо вызывает ValueError, если search не равен 'args' или 'kwargs'.
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