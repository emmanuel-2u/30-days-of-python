import re

sentence = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.'

only_digits = r'-?\d+'

all_digits_string = re.findall(only_digits, sentence)

all_digits = map(int, all_digits_string)

all_digits = sorted(all_digits)

distance = all_digits[-1] - all_digits[0]
print('Distance -', distance)