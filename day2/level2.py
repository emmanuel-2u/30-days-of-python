from math import pi

def circle_area(radius):
    return pi * (radius ** 2)

radius = 30

area_of_circle = circle_area(radius)
print('Static area of circle is', area_of_circle)

circum_of_circle = 2 * pi * radius
print('Circumference of circle is', circum_of_circle)
input_radius = None

def take_number_input(message = 'Enter radius: '):
    try:
        input_radius = float(input(message))
        return input_radius
    except ValueError:
        print('Invalid input. Try another input')

while True:
    input_number = take_number_input()
    if input_number is None:
        continue
    area_of_circle = circle_area(input_number)
    print('Area of circle is -', area_of_circle)
    break