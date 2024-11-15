'''
Даны два целых числа A и B (A < Б). Найти произведение всех целых чисел от A до
B включительно.
'''
a, b = input('Введите первое число: '), input('Ввeдите второе число: ')
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print('Неправильно ввели 1-е число')
        a = input('Введите первое число: ')

while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print('Неправильно ввели 2-е число')
        b = input('Введите второе число: ')

n = 1
for i in range(a, b+1):
    n *= i
print(f'Произведение всех числех между {a} и {b} = {n}')