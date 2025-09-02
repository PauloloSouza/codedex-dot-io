# Paulolo's Burguer 🍔

class Restaurant:
    name = ""
    category = ""
    rating = 0.0
    delivery = False

paulolos_burguer = Restaurant()

paulolos_burguer.name = "Paulolo's King Burguer"
paulolos_burguer.category = "American Diner"
paulolos_burguer.rating = 4.6
paulolos_burguer.delivery = False

system_burguer = Restaurant()

system_burguer.name = "System Lanches"
system_burguer.category = "Junk Food"
system_burguer.rating = 5.0
system_burguer.delivery = True

print(vars(paulolos_burguer))
print(vars(system_burguer))