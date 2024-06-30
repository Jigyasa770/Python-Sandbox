def planet(id):
    planets = {2: ' Venus', 1: 'Mercury', 3: 'Earth', 4: 'Mars', 5: 'Jupiter', 6: 'Saturn', 7: 'Uranus', 8: 'Neptune', 9: 'Pluto'}
    return planets[id]

id = int(input('Enter planet id: '))
p = planet(id)
print(p)