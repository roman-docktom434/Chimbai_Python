'''
Дан список размера N. Возвести в квадрат все его локальные минимумы (то есть
числа, меньшие своих соседей).
'''
import random

n = input('Введите длину списка: ')
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целое число.")
        n = input('Введите длину списка: ')

lst = [random.randint(1, 100) for _ in range(n)]

print("Сгенерированный список:", lst)
def square_local_minima(lst):
    if len(lst) < 3:
        return lst

    result = lst[:]

    for i in range(1, len(lst) - 1):
        if lst[i] < lst[i - 1] and lst[i] < lst[i + 1]:
            result[i] = lst[i] ** 2
    return  result

squared_minima = square_local_minima(lst)
print(f'Локальные минимумы в квадрате: {squared_minima}')