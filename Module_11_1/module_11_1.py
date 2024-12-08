import numpy as np

a = np.array([[1, 2, 3],[4, 5, 6]])
b = np.array([[1, 2],[3,4],[5, 6]])

c = a @ b
print(c)

d=b @ a
print(d)

"""данная библиотека упрощает работу с матрицами, хорошая бесплатная замена mathcad"""