
numbers = [1, 1, 1, 1, 1, 2, 1, 2, 4, 8, 3, 1, 3, 9, 27, 4, 1, 4, 16, 64, 5, 1, 5, 25, 125]

for num in range(0, len(numbers) - 4, 5):
    string = ''
    for i in range(5):
        string += str(numbers[num + i]) + ' '
    print(string)