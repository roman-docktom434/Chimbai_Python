"""
Описать функцию AddRightDigit(D, K), добавляющую к целому положительному
числу K справа цифру D (D — входной параметр целого типа, лежащий в диапазоне
0-9, K — параметр целого типа, являющийся одновременно входным и выходным).
С помощью этой функции последовательно добавить к данному числу K справа
данные цифры D1 и D2, выводя результат каждого добавления.
"""

def AddRightDigit(d, k):
    return int(str(k) + str(d))

k = input("Введите число K: ")
d1 = input("Введите цифру D1: ")
while type(d1) != int and type(k) != int:
    try:
        d1 = int(d1)
        k = int(k)
    except ValueError:
        print('Вы ввели не число!')
        k = input("Введите число K: ")
        d1 = input("Введите цифру D1: ")

f_sum = AddRightDigit(d1, k)
print(f"Результат после добавления {d1}: {f_sum}")

d2 = input("Введите цифру D2: ")
while type(d2) != int:
    try:
        d2 = int(d2)
    except ValueError:
        print('Вы ввели не число!')
        d2 = input("Введите цифру D2: ")

s_sum = str(f_sum) + str(d2)
print(f"Результат после добавления {d2}: {s_sum}")
