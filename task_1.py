"""
Задание 1.

Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего

Подсказка:
Для решения задачи обязательно примените коллекцию из модуля collections
Для лучшего освоения материала можете сделать
несколько варианто решения этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога
Предприятия, с прибылью ниже среднего значения: Копыта
"""

from collections import namedtuple

company_all = []


def print_company(company_numb=int(input("Введите количество предприятий"))):
    for i in range(company_numb):
        company_nm = input("Введите имя ")
        company_part = [int(n) for n in input("Введите прибыль за каждый квартал через пробел :").split()]
        company_main = namedtuple(company_nm, ["company_nm", "first_q", "second_q", "third_q", "fourth_q", "sum"])
        company_name__ = company_main(company_nm, *company_part, sum(company_part))
        company_all.append(company_name__)
    average_profit = 0
    for m in range(len(company_all)):
        average_profit += company_all[m].sum
    average_profit = average_profit // len(company_all)
    print(*(f'Предприятия, с прибылью выше среднего значения:'
            f' {company_all[a].company_nm}' for a in range(len(company_all)) if company_all[a].sum > average_profit))
    print(*(f'Предприятия, с прибылью ниже среднего значения:'
            f' {company_all[b].company_nm}' for b in range(len(company_all)) if company_all[b].sum < average_profit))
    return print(average_profit)


if __name__ == "__main__":
    print_company()
