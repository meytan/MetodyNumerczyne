import numpy as np
from numpy import polyval, arange

from readFile import read_json


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
    #generated_points = [1.5, 2.6, 3.8, 4.5]
    for x in generated_points:
        result += polyval(function, x)

    return result/n * abs(end - start)
