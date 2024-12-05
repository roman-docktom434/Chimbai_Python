'''
Дан целочисленный список размера 10. Вывести все содержащиеся в данном списке
нечетные числа в порядке возрастания их индексов, а также их количество K.
'''
numbers = []

print("Введите 10 целых чисел:")
for i in range(10):
    num = input(f"Введите число {i + 1}: ")
    while type(num) != int:
        try:
            num = int(num)
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")
            num = input(f"Введите число {i + 1} еще раз: ")
    numbers.append(num)

odd_numbers = []

for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)

print("Нечетные числа в порядке возрастания их индексов:")
for num in odd_numbers:
    print(num, end=" ")

k = len(odd_numbers)
print(f"\nКоличество нечетных чисел: {k}")