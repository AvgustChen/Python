# Реализуйте класс Matrix, представляющий матрицу и поддерживающий следующие операции:
#
# Инициализация матрицы. Конструктор класса должен принимать количество строк rows и количество столбцов cols
# и создавать матрицу с нулевыми значениями.
#
# Операция сложения матриц. Реализуйте метод __add__, который позволяет складывать две матрицы одинаковых размеров.
#
# Операция умножения матриц. Реализуйте метод __mul__, который позволяет умножать две матрицы с согласованными
# размерами (количество столбцов первой матрицы должно быть равно количеству строк второй матрицы).
#
# Сравнение матриц на равенство. Реализуйте метод __eq__, который позволяет сравнивать две матрицы на равенство.
#
# Представление матрицы в виде строки. Реализуйте метод __str__, который возвращает строковое представление матрицы,
# где элементы строки разделены пробелами, а строки сами разделены символами новой строки.
#
# Представление матрицы в виде строки для создания нового объекта. Реализуйте метод __repr__, который возвращает строку,
# которую можно использовать для создания нового объекта класса Matrix.
class Matrix:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for i in range(self.cols)] for i in range(self.rows)]

    def __add__(self, other):
        result = Matrix(self.rows, self.cols)
        result.data = [[self.data[i][j] + other.data[i][j] for j in range(len(self.data[0]))] for i in
                       range(len(self.data))]
        return result
    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError(
                "Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы для умножения.")
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result
    def __eq__(self, other):
        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                if self.data[i][j] != other.data[i][j]:
                    return False
        return True

    def __str__(self):
        return "\n".join([" ".join(map(str, x)) for x in self.data])

    def __repr__(self):
        return f'Matrix({self.rows}, {self.cols})'
