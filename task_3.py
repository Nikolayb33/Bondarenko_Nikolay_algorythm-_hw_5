"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее

2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее

3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""


from collections import deque
from timeit import timeit


lst = [i for i in range(1000)]
lst_2 = [i for i in range(100)]
deq_lst = deque(lst)
deq_lst_2 = deque(lst_2)
x = "x"

def append_lst(lst):
    for i in range(100):
        lst.append(i)
    return lst


def append_deq_lst(deq_lst):
    for i in range(100):
        deq_lst.append(i)
    return deq_lst


def pop_lst(lst):
    for i in range(10000):
        lst.pop(i)
    return lst


def pop_deq_lst(deq_lst):
    for i in range(10000):
        deq_lst.pop()
    return deq_lst


def extend_lst(lst, lst_2):
    for i in range(100):
        lst.extend(lst_2)
    return lst


def extend_deq_lst(deq_lst, deq_lst_2):
    for i in range(100):
        deq_lst.extend(deq_lst_2)
    return deq_lst


print(f'append_lst: {timeit("append_lst", globals=globals())}')
print(f'append_deq_lst: {timeit("append_deq_lst", globals=globals())}')
print(f'pop_lst: {timeit("pop_lst", globals=globals())}')
print(f'pop_deq_lst: {timeit("pop_deq_lst", globals=globals())}')
print(f'extend_lst: {timeit("extend_lst", globals=globals())}')
print(f'extend_deq_lst: {timeit("extend_deq_lst", globals=globals())}')


def insert_lst(lst):
    for i in range(1000):
        lst.insert(0, i)
    return lst


def appendleft_deq_lst(deq_lst):
    for i in range(1000):
        deq_lst.appendleft(0, i)
    return deq_lst


def popleft_lst(lst):
    for i in range(1000):
        lst.pop(i)
    return lst


def popleft_deq_lst(deq_lst):
    for i in range(1000):
        deq_lst.popleft()
    return deq_lst


def extendleft_lst(lst, lst_2):
    for i in range(100):
        for i in lst_2:
            lst.insert(0, i)
        return lst_2


def extendleft_deq_lst(deq_lst):
    for i in range(100):
        deq_lst.extendleft(i)
    return deq_lst


print('-'*20)
print(f'insert_lst: {timeit("insert_lst", globals=globals())}')
print(f'appendleft_deq_lst: {timeit("appendleft_deq_lst", globals=globals())}')
print(f'popleft_lst: {timeit("popleft_lst", globals=globals())}')
print(f'popleft_deq_lst: {timeit("popleft_deq_lst", globals=globals())}')
print(f'extendleft_lst: {timeit("extendleft_lst", globals=globals())}')
print(f'extendleft_deq_lst: {timeit("extendleft_deq_lst", globals=globals())}')


def el_from_lst(x):
    for i in range(len(lst)):
        lst[i] = x
    return x


def el_from_deq_lst(x):
    for i in range(len(deq_lst)):
        deq_lst[i] = x
    return x

print('-'*20)
print(f'el_from_lst: {timeit("el_from_lst", globals=globals())}')
print(f'el_from_deq_lst: {timeit("el_from_deq_lst", globals=globals())}')

# 1) Добавление элемента и списка происходит по времени быстрее в deque
# вытаскивание элемента происходит одинаково по времени что в deque, что в lst
# append_lst: 0.049461495
# append_deq_lst: 0.033341998
# pop_lst: 0.03116953800000001
# pop_deq_lst: 0.032273687999999995
# extend_lst: 0.038370292
# extend_deq_lst: 0.03229568099999999
# --------------------
# 2) значения почти совпадают существенной разницы нет
# insert_lst: 0.028753238999999986
# appendleft_deq_lst: 0.03042508500000002
# popleft_lst: 0.03459261899999999
# popleft_deq_lst: 0.031433288000000004
# extendleft_lst: 0.032371101999999985
# extendleft_deq_lst: 0.028420622000000006
# --------------------
# 3) значения почти совпадают, разницы существенной нет
# el_from_lst: 0.031782849
# el_from_deq_lst: 0.03573196300000003
