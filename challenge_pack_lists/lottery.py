# Lottery 💰

import random

my_numbers = []
winning_numbers = []
guessed_numbers = 0

for i in range(0,5):
    num1 = random.randint(1, 69)
    if num1 not in my_numbers:
        my_numbers.append(num1)

    num2 = random.randint(1, 69)
    if num2 not in winning_numbers:
        winning_numbers.append(num2)

num1 = random.randint(1, 26)
num2 = random.randint(1, 26)
if num1 not in my_numbers:
    my_numbers.append(num1)
if num2 not in winning_numbers:
    winning_numbers.append(num2)

for i in range(len(my_numbers)): #This for and if is self add (not requirement of exercise), going further.
    for j in range(len(winning_numbers)):
        if my_numbers[i] == winning_numbers[j]:
            guessed_numbers += 1

print(my_numbers)
print(winning_numbers)
print(f"You guessed: {guessed_numbers} numbers.") #This print is self add (not requirement of exercise)