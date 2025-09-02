#Favorite Cities 🌆

class City:
    def __init__(self, name, country, population, landmarks, founding_year, mayor):
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmarks
        self.founding_year = founding_year
        self.mayor = mayor

belo_horizonte = City ("Belo Horizonte", "Brazil", 2420000, ["Igreja da Pampulha", "Praça do Papa"], 1701, "Álvaro Damião")
peninsula_marau = City ("Península do Maraú", "Brazil", 25636, ["Praia de Barra Grande", "Piscinas Naturais"], 1705, "Dr. Ravan Barcelos")

print(vars(belo_horizonte))
print(vars(peninsula_marau))