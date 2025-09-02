#Selector Hat

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0
i = 0

while i == 0: #This while loop is self add (not requirement of exercise)
  print ("Q1) Do you like Dawn or Dusk?")
  print ("  1) Dawn")
  print ("  2) Dusk")
  answer1 = int(input("Enter your answer (1 or 2): "))
  if answer1 == 1:
    Gryffindor = Gryffindor + 2
    Ravenclaw = Ravenclaw + 2
    i = 1
  elif answer1 == 2:
    Hufflepuff = Hufflepuff + 2
    Slytherin = Slytherin + 2
    i = 1
  else:
    print ("Wrong input. Chose between 1 or 2.")
    i = 0

i = 0;
while i == 0: #This while loop is self add (not requirement of exercise)
  print("Q2) When I’m dead, I want people to remember me as:")
  print(" 1) The Good.")
  print(" 2) The Great.")
  print(" 3) The Wise.")
  print(" 4) The Bold.")
  answer2 = int(input("Enter your answer (1 to 4): "))
  if answer2 == 1:
    Hufflepuff = Hufflepuff + 3
    i = 1
  elif answer2 == 2:
    Slytherin = Slytherin + 3
    i = 1
  elif answer2 == 3:
    Ravenclaw = Ravenclaw + 3
    i = 1
  elif answer2 == 4:
    Gryffindor = Gryffindor + 3
    i = 1
  else:
    print ("Wrong input. Chose between 1 to 4.")
    i = 0

i = 0;
while i == 0: #This while loop is self add (not requirement of exercise)
  print("Q3) Which kind of instrument most pleases your ear?")
  print(" 1) The violin.")
  print(" 2) The trumpet.")
  print(" 3) The piano.")
  print(" 4) The drum.")
  answer3 = int(input("Enter your answer (1 to 4): "))
  if answer3 == 1:
    Slytherin = Slytherin + 4
    i = 1
  elif answer3 == 2:
    Hufflepuff = Hufflepuff + 4
    i = 1
  elif answer3 == 3:
    Ravenclaw = Ravenclaw + 4
    i = 1
  elif answer3 == 4:
    Gryffindor = Gryffindor + 4
    i = 1
  else:
    print ("Wrong input. Chose between 1 to 4.")
    i = 0

#Going further, challenged by codedex.
print(f"Slytherin points: {Slytherin}")
print(f"Hufflepuff points: {Hufflepuff}")
print(f"Ravenclaw points: {Ravenclaw}")
print(f"Gryffindor points: {Gryffindor}")

val = {
  "Slytherin" : Slytherin,
  "Hufflepuff" : Hufflepuff,
  "Ravenclaw" : Ravenclaw,
  "Gryffindor" : Gryffindor
}

winner = max(val, key=val.get)
print(f"The Hat decides for {winner}, welcome to yor new House")