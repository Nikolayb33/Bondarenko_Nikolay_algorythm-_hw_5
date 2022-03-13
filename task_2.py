"""
Задание 2.

Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections

defaultdict(list)
int(, 16)
reduce

2) через ООП

вспомните про перегрузку методов

__mul__
__add__
"""


class Numer_16:

    def __init__(self, numer_16):
        self.numer_16 = numer_16

    def __add__(self, other):
        add_num = 0
        new_lst = []
        to_10 = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                 '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

        to_16 = {val: key for key, val in to_10.items()}

        res_lst = []
        if len(self.numer_16) == len(other.numer_16):
            for m, n in zip(reversed(self.numer_16), reversed(other.numer_16)):
                o = (to_10[m] + to_10[n] + add_num) % 16
                if (to_10[m] + to_10[n]) > 15:
                    add_num += (to_10[m] + to_10[n]) // 16
                    new_lst.append(o)
                else:
                    new_lst.append(o)
        elif len(self.numer_16) > len(other.numer_16):
            i = 0
            while i != len(other.numer_16):
                for m, n in zip(reversed(self.numer_16), reversed(other.numer_16)):
                    o = (to_10[m] + to_10[n] + add_num) % 16
                    if (to_10[m] + to_10[n]) > 15:
                        add_num += (to_10[m] + to_10[n]) // 16
                        new_lst.append(o)
                    else:
                        new_lst.append(o)
                        add_num = 0
                    i += 1
                for x in self.numer_16[::-1][i:]:
                    o = (to_10[x] + add_num)
                    if o > 15:
                        new_lst.append(o % 16)
                        new_lst.append(o // 16)
                    else:
                        new_lst.append(o)
        elif len(self.numer_16) < len(other.numer_16):
            i = 0
            while i != len(self.numer_16):
                for m, n in zip(reversed(self.numer_16), reversed(other.numer_16)):
                    o = (to_10[m] + to_10[n] + add_num) % 16
                    if (to_10[m] + to_10[n]) > 15:
                        add_num += (to_10[m] + to_10[n]) // 16
                        new_lst.append(o)
                    else:
                        new_lst.append(o)
                        add_num = 0
                    i += 1
                for x in other.numer_16[::-1][i:]:
                    o = (to_10[x] + add_num)
                    if o > 15:
                        new_lst.append(o % 16)
                        new_lst.append(o // 16)
                    else:
                        new_lst.append(o)
        result_lst = reversed(new_lst)
        for p in result_lst:
            res_lst.append(to_16[p])
        return "".join(res_lst)

    def __mul__(self, other):
        mul = str(hex(int(self.numer_16, 16) * int(other.numer_16, 16)))
        return mul[2:].upper()


if __name__ == "__main__":
    a = Numer_16("C4F")
    b = Numer_16("A2")
    c = a * b
    d = a + b
    print(c)
    print(d)
