'''
Дан список размера N. Найти минимальный из его локальных максимумов
(локальный минимум — это элемент, который меньше любого из своих соседей).
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

local_minima = []

for i in range(1, n - 1):
    if lst[i] < lst[i - 1] and lst[i] < lst[i + 1]:
        local_minima.append(lst[i])

if local_minima:
    min_local_minimum = min(local_minima)
    print("Минимальный из локальных минимумов:", min_local_minimum)
else:
    print("Локальных минимумов не найдено.")
