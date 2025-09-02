# Write code below 💖

fast_food_menu =[
    "🍔 Cheeseburger",
    "🍟 Fries",
    "🥤 Soda",
    "🍦 Ice Cream",
    "🍪 Cookie"
  ]

def welcome():
  print("Welcome to PauloloSouza Fast Food")
  print(fast_food_menu)

def get_item():
  i = int(input("What lunch do you want today?"))
  selected = fast_food_menu[i-1]
  return selected

welcome()
print(f"You choose " + get_item())