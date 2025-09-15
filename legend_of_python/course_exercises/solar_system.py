#Solar System

# from random import sample
# famous_houses = [
#   '🐺 Stark',
#   '🐉 Targaryen',
#   '🦌 Baratheon',
#   '🦑 Greyjoy',
#   '🦁 Lannister'
# ]
# example = sample(famous_houses, 2)
# print(f'Example: {example}')

from math import pi
from random import choice as ch

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

random_planet = ch(planets)

if random_planet == "Mercury":
    r = 2440
elif random_planet == "Venus":
    r = 6052
elif random_planet == "Earth":
    r = 6371
elif random_planet == "Mars":
    r = 3390
elif random_planet == "Saturn":
    r = 58232
area = 4*pi*r

print(round(area, 2))