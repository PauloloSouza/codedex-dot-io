# Pokedéx 📟

class Pokedex:
    def __init__(self, entry, name, types , description, is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught

    def speak(self):
        print(self.name + ", " + self.name)
    
    def display_details(self):
        print("Entry number: " + str(self.entry))
        print("Name: " + self.name)
        print("Type: " + str(self.types))
        print("Description: " + self.description)
        if self.is_caught == True:
            print(self.name + " has already been caught!")
        else:
            print(self.name + " hasn't been caught yet!")

pikachu = Pokedex(25, "Pikachu", "Eletric", "When it is angered, it immediately discharges the energy stored in the pouches in its cheeks.", True)
mewtwo = Pokedex(15, "Mewtwo", "Psychic", "Its DNA is almost the same as Mew's. However, its size and disposition are vastly different.", False)
maril = Pokedex(183, "Maril", ["Water", "Fairy"], "The fur on its body naturally repels water. It can stay dry even when it plays in the water.", True)

pikachu.speak()
pikachu.display_details()
mewtwo.speak()
mewtwo.display_details()
maril.speak()
maril.display_details()