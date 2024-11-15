'''
Спортсмен-лыжник начал тренировки, пробежав в первый день 10 км. Каждый
следующий день он увеличивал длину пробега на P процентов от пробега
предыдущего дня (P — вещественное, 0< P <50). По данному P определить, после
какого дня суммарный пробег лыжника за все дни превысит 200 км, и вывести
найденное количество дней K (целое) и суммарный пробег S (вещественное число).
'''

f_day = 10
p = (input('Введите увеличение длины пробега (увеличивается в процентах): '))
while type(p) != float:
    try:
        p = float(int(p))
    except ValueError:
        print('Вы ввели не число!')
        p = (input('Введите увеличение длины пробега (увеличивается в процентах): '))
days = 1
while f_day < 200:
    f_day = f_day + (f_day * p / 100)
    days += 1
print(f'Количество дней - {days}\n'
      f'Суммарный пробег - {f_day}')