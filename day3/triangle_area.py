import sys, os

path = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(path)

from utils.take_number_input import take_number_input

def validate(message = 'Enter height: '):
    value = take_number_input(message)
    if (value is None):
        print('Invalid value')
        exit()
    return value

base = validate('Enter base: ')
height = validate()

triangle_area = 0.5 * base * height
print('Triangle area ', triangle_area)