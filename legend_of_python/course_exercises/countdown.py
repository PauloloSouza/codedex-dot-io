#Countdown
import random
import datetime

today = datetime.date.today()
print(today)
next_birthday = datetime.date(2026, 1, 27)

bday_messages = [
  "Hope you have a very Happy Birthday! 🎈",
  "It's your special day – get out there and celebrate! 🎉",
  "You were born and the world got better – everybody wins! 🥳",
  "Have lots of fun on your special day! 🎂",
  "Another year of you going around the sun! 🌞"
]

random_message = random.choice(bday_messages)

time_difference = next_birthday - today

if today == next_birthday:
    print(random_message)
else:
    print(f"My next birthday is {time_difference} days away")