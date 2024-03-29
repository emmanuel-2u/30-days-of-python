import re

def is_valid_variable(name):
    valid_variable = r'[a-zA-Z_]\w*'
    print(re.match(valid_variable, name) != None)

is_valid_variable('first_name') # True
# Somehow, this is returning True instead of False
is_valid_variable('first-name') # False
is_valid_variable('1first_name') # False
is_valid_variable('firstname') # True

# - Keep your eyes open during your flip so you can see to stick your landing.
# - Bring your chest up as you land to help you stay balanced
# - Keep your knees bent as you come in for your landing
# - Swing your arms behind you, stopping when they’re just behind your back.
# - Land with your hips under your chest and your knees aligned with your ankles
# - Stretch out your legs about 3/4 of the way through your rotation
# - Bring your arms forward and over your head as you leap upwards
# - Grab your knees with your hands to secure your tuck.
# - Pull your knees toward your chest at the peak of your jump.
# - Find a soft surface, such as a gymnastics mat or foam pit.
# - Focus your gaze on an object in the distance.
# - Bend at your knees into a high squat.
# - Stretch your muscles before you jump to prevent injuries.
# - Use a spotter for maximum safety.
# - Stand with your feet shoulder-width apart and your arms stretched overhead.