"""
Задание 7
Создайте класс «Матрица», который имеет атрибуты количества строк и столбцов.
Добавьте методы для сложения, вычитания и умножения матриц.
"""
class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for j in range(cols)] for i in range(rows)]
    
    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])
    
    def set_data(self, data):
        if len(data) != self.rows or len(data[0]) != self.cols:
            raise ValueError("Размерность данных не соответствует размерности матрицы")
        self.data = data

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны быть одинакового размера для сложения")
        
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны быть одинакового размера для вычитания")
        
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] - other.data[i][j]
        return result

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы")
        
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result

if __name__ == "__main__":
    m1 = Matrix(2, 2)
    m2 = Matrix(2, 2)

    m1.set_data([[1, 2], [3, 4]])
    m2.set_data([[5, 6], [7, 8]])

    print("Матрица 1:")
    print(m1)
    print("\nМатрица 2:")
    print(m2)

    print("\nСложение матриц:")
    print(m1 + m2)

    print("\nВычитание матриц:")
    print(m1 - m2)

    print("\nУмножение матриц:")
    print(m1 * m2)