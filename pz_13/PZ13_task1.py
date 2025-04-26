'''
В двумерном списке элементы строки N (N задать с клавиатуры) увеличить на 3.
'''
import random

rows_count = 4
cols_count = 3

matrix = [
    [random.randint(0, 9) for col_index in range(cols_count)]
    for row_index in range(rows_count)
]

print("Исходная матрица:")
for row in matrix:
    print(" ".join(str(value) for value in row))

chosen_row = int(input("Введите номер строки (1..4), элементы которой увеличить на 3: ")) - 1

new_matrix = [
    [
        value + 3 if row_index == chosen_row else value
        for value in matrix[row_index]
    ]
    for row_index in range(rows_count)
]

print("\nРезультат:")
for row in new_matrix:
    print(" ".join(str(value) for value in row))
