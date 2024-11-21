"""
Найти сумму чисел ряда 1,2,3,4,... от числа n до числа m. Суммирование оформить
функцией с параметрами. Значения n и m программа должна запрашивать.
"""
def sum_range(n, m):
    return sum(range(n, m + 1))

f_num = input('Введите число n: ')
s_num = input('Введите число m: ')
while type(f_num) != int and type(s_num) != int:
    try:
        f_num = int(f_num)
        s_num = int(s_num)
    except ValueError:
        print('Вы ввели не число!')
        f_num = input('Введите число n: ')
        s_num = input('Введите число m: ')

result = sum_range(f_num, s_num)
print(f'Сумма чисел от {f_num} до {s_num} равна: {result}')
