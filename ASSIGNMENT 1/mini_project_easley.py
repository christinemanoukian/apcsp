planet = input('Pick a planet in the Solar System: ')

while planet not in ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']:
    print('Input not valid. Make sure to capitalize the first letter only of the planet.')
    planet = input('Pick a planet in the Solar System: ')

age = int(input('Enter your age: '))

planet_age = None

if planet == 'Mercury':
    planet_age = age * 365 / 88
elif planet == 'Venus':
    planet_age = age * 365 / 225
elif planet == 'Earth':
    planet_age = age
elif planet == 'Mars':
    planet_age = age * 365 / 687
elif planet == 'Jupiter':
    planet_age = age * 12
elif planet == 'Saturn':
    planet_age = age * 29
elif planet == 'Uranus':
    planet_age = age * 84
elif planet == 'Neptune':
    planet_age = age * 165

planet_age = round(planet_age)


print('You are ' + str(planet_age) + ' years old on ' + str(planet) + '!')

