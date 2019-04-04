import json


def read_points(filename="./resources/points.txt"):
    try:
        file = open(filename, 'r')
    except FileNotFoundError as e:
        print(e)
        return []
    else:
        lines = file.readlines()
        file.close()

    lines = [x.strip().split() for x in lines]
    points = [(float(x[0]), float(x[1])) for x in lines]

    return points


def read_function(filename="./resources/function.txt"):
    try:
        file = open(filename, 'r')
    except FileNotFoundError as e:
        print(e)
        return []
    else:
        lines = file.readlines()
        file.close()

    return [x.strip() for x in lines]


def read_json(key):
    with open('./resources/test.json') as json_file:
        data = json.load(json_file)
        return data[key]

