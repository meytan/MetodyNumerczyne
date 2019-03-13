import readFile


def interpolation(searched_point, points=readFile.read_points()):
    value = 0
    for point in points:
        tmp = 1
        for point2 in points:
            if point2 != point:
                tmp *= ((searched_point - point2[0]) / (point[0] - point2[0]))
        value += tmp * point[1]

    return value
