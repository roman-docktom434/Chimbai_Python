m = input("Введите массу в килограммах: ")
while type(m) != int:
        try:
            m = int(m)
        except ValueError:
            print("Ошибка! Введите число!")
            m = input("Введите массу в килограммах: ")
tons = m // 1000
print("Полных тонн: ", tons)
