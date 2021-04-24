from itertools import zip_longest


class Matrix(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.matrix])

    def __add__(self, value):
        return Matrix(list(map(
            lambda a, b: list(map(lambda c, d: c + d, a, b)),
            self.matrix, value.matrix)))


matrix_1 = Matrix([[1, 2, ], [3, 4], [5, 6]])
matrix_2 = Matrix([[7, 8, ], [9, 10], [11, 12]])
print(matrix_1)
print()
print(matrix_1 + matrix_2)
