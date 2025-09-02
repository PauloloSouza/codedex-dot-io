#Food Ratings

rating = float(2)

if rating > 4.5:
  print("Extraordinary")
elif rating > 4 and rating < 4.6:
  print("Excellent")
elif rating > 3 and rating < 4.1:
  print("Good")
elif rating > 2 and rating < 3.1:
  print("Fair")
else:
  print("Poor!!")