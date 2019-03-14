import readFile


def lagrange_interpolation(searched_point, points=readFile.read_points()):
    value = 0
    for point in points:
        tmp = 1
        for point2 in points:
            if point2 != point:
                tmp *= ((searched_point - point2[0]) / (point[0] - point2[0]))
        value += tmp * point[1]

    return value


def difference_quotient(points):
    tab =[points[0][1]]

    last_row = [y[1] for y in points]

    for x in range(0, len(points)-1):
        tmp_row = []
        for i in range(0, len(last_row)-1):

            a = last_row[i+1] - last_row[i]
            b = points[i+1+x][0] - points[i][0]
            tmp_row.append(a/b)
        last_row = tmp_row
        tab.append(last_row[0])
    return tab


def newton_interpolation(searched_point, points=readFile.read_points()):
    values = difference_quotient(points)
    result = 0
    for i in range(0,len(values)):
        tmp = values[i]
        for j in range(0,i):
            tmp*= (searched_point-points[j][0])
        result+=tmp
    return  result
