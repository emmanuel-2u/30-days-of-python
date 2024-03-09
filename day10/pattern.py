
def print_pattern(length):
    for i in range(length):
        string = ''
        for j in range(i + 1):
            string += '#'
        print(string)

print_pattern(7)