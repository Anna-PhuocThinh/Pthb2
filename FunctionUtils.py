import math


def ptb2(a,b,c):
    delta = float(b * b - 4 * a * c)
    if (a == 0):
        if (b == 0 and c != 0):
            x1 = x2 = "Vo nghiem"
        elif (b == 0 and c == 0):
            x1 = x2 = "Vo so nghiem"
        else:
            x = float(-c / b)
            x1 = x2 = x
    else:
        if (delta < 0):
            x1 = x2 = "Vo nghiem"
        elif (delta == 0):
            x1 = x2 = float(-b / 2 * a)
        else:
            x1 = float((-b + math.sqrt(delta)) / (2 * a))
            x2 = float((-b - math.sqrt(delta)) / (2 * a))
    return x1, x2