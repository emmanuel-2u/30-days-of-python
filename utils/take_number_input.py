def take_number_input(message = 'Enter radius: '):
    try:
        input_radius = float(input(message))
        return input_radius
    except ValueError:
        print('Invalid input. Try another input')