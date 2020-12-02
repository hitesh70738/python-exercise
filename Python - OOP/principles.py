class Animals:
    

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    def breathe(self):
        return f"{self.name} breathes."


class Mammal(Animals):
    def __init__(self, name, age, weight, legs):
        super().__init__(name, age, weight)
        self.legs = legs

class Dog(Mammal):
    def breathe(self):
        return f"{self.name} pants."



animal = Animals("Bill", "9", 130)

print(animal.name)


mammal = Mammal("Bob", 10, 150, 4)

print(mammal.legs)


dog = Dog("Chewbarka", 4, 70, 4)

print(animal.breathe())
print(dog.breathe())