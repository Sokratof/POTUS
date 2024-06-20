"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    return [num*2 for num in args]

print(power_numbers(*power_numbers()))


    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers():
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def filter_numbers(numbers:int, filter_type:str):
    if filter_type == "ODD":
        return [num for num in numbers if num % 2 != 0]
    elif filter_type == "EVEN":
        return [num for num in numbers if num % 2 == 0]
    elif filter_type =="PRIME":
        return [num for num in numbers if is_prime(num)]


print(filter_numbers(numbers, "ODD"))
print(filter_numbers(numbers, "EVEN"))
print(filter_numbers(numbers, "PRIME"))