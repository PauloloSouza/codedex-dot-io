#Planet Weights

earth_weight = float(input("Enter your wheight on Earth: "))
planet = int(input("Enter your planet destination: "))

if planet == 1:
  destination_weight = earth_weight * 0.38
  print(f"In this planet your Weight is: {destination_weight}")
elif planet == 2:
  destination_weight = earth_weight * 0.91
  print(f"In this planet your Weight is: {destination_weight}")
elif planet == 3:
  destination_weight = earth_weight * 0.38
  print(f"In this planet your Weight is: {destination_weight}")
elif planet == 4:
  destination_weight = earth_weight * 2.53
  print(f"In this planet your Weight is: {destination_weight}")
elif planet == 5:
  destination_weight = earth_weight * 1.07
  print(f"In this planet your Weight is: {destination_weight}")
elif planet == 6:
  destination_weight = earth_weight * 0.89
  print(f"In this planet your Weight is: {destination_weight}")
elif planet == 7:
  destination_weight = earth_weight * 1.14
  print(f"In this planet your Weight is: {destination_weight}")
else:
  print("Invalid planet number")