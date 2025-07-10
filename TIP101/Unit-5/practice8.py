# OOP and Linked Lists
# I am going to UNDERSTAND THIS SHIT
# ONCE AND FOR ALL

# Problem 1: Pokemon Class
# Create an instance of the class: Pikachu as the name and Electric as the type
# O(1)
class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False
    
    def print_pokemon(self):
        print({
            "name": self.name,   # Output: "name": "Squirtle",
            "types": self.types, # Output: "types": ["Water"],
            "is_caught": self.is_caught # Output: "is_caught": False
        })
    
    def catch(self):
        self.is_caught = True
    
    def choose(self):
        if self.is_caught:
            print(f"{self.name} I choose you!")
        else:
            print(f"{self.name} is wild! Catch them if you can!")

    def add_type(self, new_type):
        if new_type not in self.types:
            self.types.append(new_type)

#Outside of Pokemon class:
def get_by_type(my_pokemon, pokemon_type):
    
    found = []

    for pokemon in my_pokemon:
        if pokemon_type in pokemon.types:
            found.append(pokemon)
    
    return found



pokemon1 = Pokemon("Pikachu", ["Electric"])
print(pokemon1.name)
print(pokemon1.types)

#-----------------------------

# Problem 2: Create Squirtle
# Add new instance, Squirtle, and use the method print_pokemon
# O(1)

pokemon2 = Pokemon("Squirtle", ["Water"]) 
pokemon2.print_pokemon() # has not been caught yet

#-----------------------------

# Problem 3: Is Caught
# Update squirtle so that 'is_caught' is True.
# Use print_pokemon() to verify that

# use DIRECT ASSGINMENT
pokemon2.is_caught = True
pokemon2.print_pokemon() # updated: has been caught

#-----------------------------

# Problem 4: Catch Pokemon
# new method catch(), takes no parameter but 'self'
# updates 
# my_pokemon = Pokemon("Rattata", ["Normal"])
# my_pokemon.print_pokemon()

# my_pokemon.catch()
# my_pokemon.print_pokemon()

#-----------------------------

# Problem 5: Choose Pokemon
# new method: choose()
# prints "<Pokemon name> I choose you!"
# otherwise, pokemon is wild: "<Pokemon name> is wild! Catch them if you can!"

my_pokemon = Pokemon("rattata", ["Normal"])
my_pokemon.print_pokemon()

my_pokemon.choose()
my_pokemon.catch()
my_pokemon.choose()

# Pokemon 6: Add Pokemon Type
# new method: add_type(), takes in string new_type as paramater

# # example usage
# jigglypuff = Pokemon("Jigglypuff", ["Normal"])
# jigglypuff.print_pokemon()

# jigglypuff.add_type("Fairy")
# jigglypuff.print_pokemon()

# Problem 7: Get Pokemon
# new method: get_by_type(), parameters : my_pokemon - list, pokemon_type - string

# example usage
jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
diglett = Pokemon("Diglett", ["Ground"])
meowth = Pokemon("Meowth", ["Normal"])
pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
blastoise = Pokemon("Blastoise", ["Water"])

my_pokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
normal_pokemon = get_by_type(my_pokemon, "Normal")
print(normal_pokemon)

