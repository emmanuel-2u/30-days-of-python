import sys, os

path = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(path)

from utils.take_number_input import take_number_input

sideA = take_number_input('Enter side A: ')
sideB = take_number_input('Enter side B: ')
sideC = take_number_input('Enter side C: ')

print('Perimeter is ', (sideA + sideB + sideC))