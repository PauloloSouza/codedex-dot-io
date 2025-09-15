#Slot Machine

import random

dice = [1, 2, 3, 4, 5, 6]

print(random.choices(dice, k=3))

symbols = [
  '🍒',
  '🍇',
  '🍉',
  '7️⃣'
]

def play():

    results = random.choices(symbols, k=3)

    print(f"{results[0]} | {results[1]} | {results[2]}")

    if (results[0] == "7️⃣" and results[1] == "7️⃣" and results[2] == "7️⃣"):
        print("Jackpot! 💰")
    else:
        print("Thanks for playing!")

answer = ""
while answer != "N":
    play()
    answer = input("Wanna play again? (Y/N)")