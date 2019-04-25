import numpy as np


def system_of_equation_cramer(matrix):

    matrix_w = [row[:-1] for row in matrix]
    matrix_fx = [row[-1:] for row in matrix]
    w = round(np.linalg.det(matrix_w))
    wi_list = []

    for i in range(0,len(matrix_w)):
        tmp_matrix = [x[:] for x in matrix_w]
        for j in range(0, len(tmp_matrix)):
            tmp_matrix[j][i] = matrix_fx[j][0]

        wi_list.append(round(np.linalg.det(tmp_matrix)))
    if w == 0:
        if all(i == 0 for i in wi_list):
            print("This system has infinite amount of solutions!")
        else:
            print("This system has no solution")
        return None
    return [i/w for i in wi_list]


def system_of_equation_gauss(matrix):
    for i in range(len(matrix)-1):
        for j in range (i+1, len(matrix)):
            coefficient = matrix[j][i]/matrix[i][i]
            for k in range(i, len(matrix[0])):
                matrix[j][k] = matrix[j][k] - matrix[i][k]*coefficient
    results = []
    for z in range(len(matrix)-1, -1, -1):
        x1 = matrix[z][len(matrix)]
        x2 = matrix[z][z]
        for l in range(z, len(matrix)-1):
            result = results[l-z]
            a =matrix[z][l+1]
            x1 = x1 - a * result
        results = [x1/x2] + results
    return results
