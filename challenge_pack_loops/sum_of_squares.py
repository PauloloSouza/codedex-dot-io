#Sum of Squares

number = int(input("Set a number: "))
total = 0

for i in range(1, number + 1):
  square = i ** 2
  total += square

print(total)