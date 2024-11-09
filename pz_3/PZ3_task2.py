'''
Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 — 
миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер. Дан номер единицы массы (целое 
число в диапазоне 1-5) и масса тела в этих единицах (вещественное число). Найти 
массу тела в килограммах.
'''

kil, mil, gr, tonna, centner = '1 - килограмм', '2 - миллиграмм', '3 - грамм', '4 - тонна', '5 - центнер'
massa1 = input("Введите свое ЦЕЛОЕ число: ")
while type(massa1) != int: #Обработка исключений
    try:
        massa1 = int(massa1)
    except ValueError:
        print('Вы ввели не число!')
        massa1 = input("Введите свое ЦЕЛОЕ число: ")
u_massa = input(f'Какую единицу массы Вы переводите в килограммы?\n{kil.title()}\n{mil.title()}\n{gr.title()}\n{tonna.title()}\n{centner.title()}\nВведите цифру: ')
while type(u_massa) != int: #Обработка исключений
    try:
        u_massa = int(u_massa)
    except ValueError:
        print('Вы ввели не число!')
        u_massa = input("Введите свое ЦЕЛОЕ число: ")
if u_massa == 1:
  print(f'У вас {massa1} килограмм ')
if u_massa == 2:
  print(f'У вас {massa1 / 1000000} килограмм')
if u_massa == 3:
  print(f'У вас {massa1 / 1000} килограмм')
if u_massa == 4:
  print(f'У вас {massa1 * 1000} киллограмм')
if u_massa == 5:
  print(f'У вас {massa1 * 100} килограмм')
