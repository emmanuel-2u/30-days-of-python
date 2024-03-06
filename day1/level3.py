from math import sqrt

# (2, 3) and (10, 8)
x1, y1, x2, y2 = 2, 3, 10, 8

def euclidean_distance(x1, y1, x2, y2):
    x_coord = pow((x2 - x1), 2)
    y_coord = pow((y2 - y1), 2)
    result = sqrt(x_coord + y_coord)
    return result

distance = euclidean_distance(x1, y1, x2, y2)
print('Euclidean distance of constant values is - ', distance)