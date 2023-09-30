# Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных),
# которые вы уже решали. Превратите функции в методы класса, а параметры в свойства.
# Задания должны решаться через вызов методов экземпляра.

class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def trans_matrix(self):
        result = [[0 for i in range(len(self.matrix_list))] for i in range(len(self.matrix_list[0]))]
        for i in range(len(self.matrix_list)):
            for j in range(len(self.matrix_list[0])):
                result[j][i] = self.matrix_list[i][j]
        self.matrix_list = result

    def show_matrix(self):
        for i in self.matrix_list:
            print(i)

matrix = [[1, 2],
              [3, 4],
              [5, 6],
              [7, 8]]

matrix1 = Matrix(matrix)
matrix1.show_matrix()
matrix1.trans_matrix()
matrix1.show_matrix()
matrix1.trans_matrix()
matrix1.show_matrix()
