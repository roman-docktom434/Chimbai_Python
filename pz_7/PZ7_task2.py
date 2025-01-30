'''
Дана строка, содержащая полное имя файла, то есть имя диска, список каталогов
(путь), собственно имя и расширение. Выделить из этой строки расширение файла
(без предшествующей точки)
'''
filename = input("Введите полное имя файла: ")
dot_index = filename.find('.')
if dot_index != -1:
    dot_index = filename[::-1].find('.')
    extension = filename[-dot_index:] if dot_index != -1 else ""
else:
    extension = ""

print("Расширение файла:", extension)
