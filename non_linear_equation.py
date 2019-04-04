import json
from readFile import read_json


def fun(x):
    y=0
    function = read_json("function")
    for i in range(0,len(function)):
        y = y + function[i] * (x ** (len(function) - 1 - i))
    return y


def pfun(x):
    y = 0
    function = read_json("derivative")
    for i in range(0, len(function)):
        y = y + function[i] * (x ** (len(function) - 1 - i))
    return y


def bisection():
    a, b = read_json("range")
    accuracy = read_json("accuracy")
    x = a + b / 2
    while abs(a-b) > accuracy:
        if fun(x)==0:
            return x
        if fun(x)*fun(a)<0:
            b = x
        else:
            a = x
        x = (a + b )/ 2
    return x


def nm_method():
    a, b = read_json("range")
    accuracy = read_json("accuracy")
    x = read_json("start")
    x1 = x - (fun(x)/pfun(x))
    while abs(fun(x))>=accuracy and abs(x1-x)>=accuracy:
        x=x1
        x1 = x - (fun(x)/pfun(x))

    return x1



