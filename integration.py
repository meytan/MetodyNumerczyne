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
    return result * 1
