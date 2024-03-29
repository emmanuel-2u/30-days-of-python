from math import floor

def is_prime(number):
    if (number < 1):
        return False
    if (number == 1):
        return False
    if (number == 2):
        return True
    stop = floor(number / 2)
    if stop < 3:
        return not (number % 2 == 0)
    checks = range(2, stop)
    for num in checks:
        if number % num == 0:
            return False
    return True

for num in range(5004):
    print(num, is_prime(num))