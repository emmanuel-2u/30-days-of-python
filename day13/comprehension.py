

def only_positive(list):
    return [num for num in list if num > 0]

def to_one_dimension(list):
    return [num for d1 in list for d2 in d1 for num in d2]

def create_tuple(length = 11):
    return [(value, 1, value, pow(value, 2), pow(value, 3), pow(value, 4), pow(value, 5)) for value in range(length)]

print(only_positive([-4, -3, -2, -1, 0, 2, 4, 6]))

print(to_one_dimension([[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]))

print(create_tuple())