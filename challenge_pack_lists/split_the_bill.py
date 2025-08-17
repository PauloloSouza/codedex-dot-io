#Split the Bill
import math

total_bill = 0
bill = [13.99, 28.75, 9.99, 9.99, 6.95, 7.45, 16.45, 16.45]

for i in bill:
    total_bill += i

print(total_bill)

shared_bill = total_bill / 4

print(shared_bill)
print(round(shared_bill))
