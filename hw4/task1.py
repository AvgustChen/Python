# Напишите функцию для транспонирования матрицы

def trans_matrix(matrix: list):
    result = [[0 for i in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[j][i] = matrix[i][j]
    return result



matrix = [[1,2],
          [3,4],
          [5,6],
          [7,8]]
for i in matrix:
    print(i)

print()

matrix2 = trans_matrix(matrix)
for i in matrix2:
    print(i)
