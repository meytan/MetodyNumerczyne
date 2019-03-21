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



