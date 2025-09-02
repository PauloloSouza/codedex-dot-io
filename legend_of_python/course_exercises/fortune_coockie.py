import random

#Challenged by codedex.io to solve this exercise withou an if/elif/else 

i = random.randint(0,6)

fortune_coockie = ["Don't pursue happiness - create it.",
"All things are difficult before they are easy.",
"The early bird gets the worm, but the second mouse gets the cheese.",
"Someone in your life needs a letter from you., Don't just think. Act!",
"Your heart will skip a beat.",
"The fortune you search for is in another cookie.",
"Help! Im being held prisoner in a Chinese bakery!"]

def fortune():
    print(i)
    print(fortune_coockie[i])

fortune()