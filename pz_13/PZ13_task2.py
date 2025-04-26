'''
В двумерном списке элементы последнего столбца заменить на -1.
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

new_matrix = [
    [
        -1 if col_index == cols_count - 1 else matrix[row_index][col_index]
        for col_index in range(cols_count)
    ]
    for row_index in range(rows_count)
]

print("\nРезультат:")
for row in new_matrix:
    print(" ".join(str(value) for value in row))
