#Question Six


def distance(poly1, poly2):
    import math
        
    x1 = poly1[0]
    y1 = poly1[1]
    x2 = poly2[0]
    y2 = poly2[1]
        
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


x = print(distance((-3, 8), (-1, 4)))


