"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.

Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit


# print(dir({'Наташа': 1, 'Коля': 2}))
# print(dir(OrderedDict({'Наташа': 1, 'Коля': 2})))


def dict_pop():
    new_dict = {'Наташа': 1, 'Коля': 2}
    new_dict.popitem()


def ordered_dict_pop():
    ord_dict = OrderedDict({'Наташа': 1, 'Коля': 2})
    ord_dict.popitem()


def dict_items():
    new_dict = {'Наташа': 1, 'Коля': 2}
    new_dict.items()


def ordered_dict_items():
    ord_dict = OrderedDict({'Наташа': 1, 'Коля': 2})
    ord_dict.items()


print(timeit("dict_pop()", globals=globals(), number=100000))
print(timeit("dict_items()", globals=globals(), number=100000))
print("-"*20)
print(timeit("ordered_dict_pop()", globals=globals(), number=100000))
print(timeit("ordered_dict_items()", globals=globals(), number=100000))

# смысла использовать ordered_dict нету
