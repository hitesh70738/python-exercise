class Dog:
    def __init__(self, name, breed, energy):
        self.name = name
        self.breed = breed
        self.energy = energy

    def bark(self):
        if self.energy < 5:
            return f"{self.name} gentley boofs!"
        else:
            return f"{self.name} barks hartly!"

my_dog = Dog("Chewbarka", "Newfoundland", 3)

print(my_dog.name)
print(my_dog.bark())


