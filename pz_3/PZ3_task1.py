a,b,c = input('Введите число A: '), input('Введите число B: '), input('Введите число C: ')
while type(a) != int and type(b) != int and type(c) != int:
    try:
        a = int(a)
        b = int(b)
        c = int(c)
    except ValueError:
        print('Ошибка: введите целое число.')
        a = input('Введите число A: ')
        print('Ошибка: введите целое число.')
        b = input('Введите число B: ')
        print('Ошибка: введите целое число.')
        c = input('Введите число C: ')

if (a > b > c) or (c > b > a):
        print('Число B находится между числами A и C.')
else:
    print('Число B не находится между числами A и C.')