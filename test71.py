from copy import deepcopy
import random

class Matrix:

    def __init__(self, list):
        self.matrix = deepcopy(list)

    def __str__(self):
        string = ""
        for row in self.matrix:
            for columm in row:
                string = f"{string}{columm}  "
            string = string + "\n"
        return string

    def __add__(self, other):
        addmatrix = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[i]))] for i in range(len(self.matrix))]
        return Matrix(addmatrix)


quan_row = random.randint(1, 5)
quan_colum = random.randint(1, 5)
a = Matrix([[random.randint(-100, 100) for _ in range(quan_colum)] for _ in range(quan_row)])
print("Матрица A : \n", a)
b = Matrix([[random.randint(-100, 100) for _ in range(quan_colum)] for _ in range(quan_row)])
print("Матрица B : \n", b)
print("Матрица A + B : \n", a + b)

