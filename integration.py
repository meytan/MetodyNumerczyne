import numpy as np
from numpy import polyval, arange

from readFile import read_json, read_points


def square_integration(file):
    result = 0
    n = read_json(file, "number")
    start, end = read_json(file, "range")
    function = read_json(file, "function")
    dx = (end-start)/n
    for x in arange(start+dx, end+dx, dx):
        pol = polyval(function, x)
        result = result + pol
    return result * dx


def trapeze_integration(file):
    result = 0
    n = read_json(file, "number")
    start, end = read_json(file, "range")
    function = read_json(file, "function")
    dx = (end - start) / n
    for x in arange(start, end, dx):
        pol = (polyval(function, x) + polyval(function, x + dx))/2
        result = result + dx * pol
    return result


def simpson_integration(file):
    result = 0.0
    n = read_json(file, "number") *2
    start, end = read_json(file, "range")
    function = read_json(file, "function")
    h = (end - start) / n
    for x in arange(start, end, 2*h):
        pol = polyval(function, x) + 4*polyval(function, x + h) + polyval(function, x + 2*h)
        result = result + h / 3 * pol
    return result


def monte_carlo_integration(file):
    result = 0.0
    n = read_json(file, "number")
    start, end = read_json(file, "range")
    function = read_json(file, "function")
    generated_points = np.random.uniform(start, end, n)
    # generated_points = [1.5, 2.6, 3.8, 4.5]
    for x in generated_points:
        result += polyval(function, x)

    return result/n * abs(end - start)


def gauss_quadrature_2d():
    real_points = read_points("./resources/gauss")
    weight1, weight2 = 1, 1
    points = (-0.5773502692, 0.5773502692)
    ksi_derivetive = [[0, 0, 0, 0], [0, 0, 0, 0]]
    ni_derivetive = [[0, 0, 0, 0], [0, 0, 0, 0]]
    fun_detj = [[0, 0], [0, 0]]
    for j in [0, 1]:
        for i in [0, 1]:
            ksi_derivetive[j][0] = -0.25*(1.0-points[j])
            ksi_derivetive[j][1] = 0.25*(1.0-points[j])
            ksi_derivetive[j][2] = 0.25*(1.0+points[j])
            ksi_derivetive[j][3] = -0.25*(1.0+points[j])
            ni_derivetive[i][0] = -0.25*(1.0-points[i])
            ni_derivetive[i][1] = -0.25*(1.0+points[i])
            ni_derivetive[i][2] = 0.25*(1.0+points[i])
            ni_derivetive[i][3] = 0.25*(1.0-points[i])

    for j in [0, 1]:
        for i in [0, 1]:
            dxdKSI = ksi_derivetive[j][0]*real_points[0][0] + ksi_derivetive[j][1] * real_points[1][0]+ ksi_derivetive[j][2] * real_points[2][0] + ksi_derivetive[j][3] * real_points[3][0]
            dydKSI = ksi_derivetive[j][0]*real_points[0][1] + ksi_derivetive[j][1] * real_points[1][1]+ ksi_derivetive[j][2] * real_points[2][1] + ksi_derivetive[j][3] * real_points[3][1]
            dxdNI = ni_derivetive[j][0]*real_points[0][0] + ni_derivetive[j][1] * real_points[1][0]+ ni_derivetive[j][2] * real_points[2][0] + ni_derivetive[j][3] * real_points[3][0]
            dydNI = ni_derivetive[j][0]*real_points[0][1] + ni_derivetive[j][1] * real_points[1][1]+ ni_derivetive[j][2] * real_points[2][1] + ni_derivetive[j][3] * real_points[3][1]

            fun_detj[i][j] = dxdKSI*dydNI - dxdNI*dydKSI

    area = 0

    for j in [0, 1]:
        for i in [0, 1]:
            area += abs(fun_detj[i][j])*weight1*weight2

    return area
