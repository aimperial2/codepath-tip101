class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("Woof!")

dog1 = Dog("Fido", "Black lab", "Alan Turing")
dog2 = Dog("Rex", "German Shepherd", "Ada Lovelace")

dog1.bark()
dog2.bark()