"""
Из предложенного текстового файла (text18-7.txt) вывести на экран его содержимое,
количество букв в нижнем регистре. Сформировать новый файл, в который поместить текст
в стихотворной форме предварительно поставив последнюю строку между второй и
третьей.
"""
with open("text18-7.txt", "r", encoding="utf-16") as f:
    lines = f.read().splitlines()
null = 0
for line in lines:
    for i in line:
        if i.isalpha() and i.islower():
            null += 1
first = lines[0]
last = '\n'+lines[-1]
other_rows = '\n'.join(lines[1:-1])
print(f'Количество букв в нижнем регистре: {null}')
with open('new_text18-7.txt', 'w') as file:
    file.write(first)
    file.write(last+'\n')
    file.write(other_rows)
    file.write(f'\n\n\nКоличество букв в нижнем регистре: {str(null)}')