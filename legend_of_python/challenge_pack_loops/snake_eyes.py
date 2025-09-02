#Snake Eyes

import random

total = 0
i = 0 #added a variabel to count attempts, until rolls "Snake Eyes!"

while total != 2:
  i = i + 1
  die1 = random.randint(1,6)
  die2 = random.randint(1,6)
  total = die1 + die2
  print(f"{i} - Nope")
print("Snake Eyes!")