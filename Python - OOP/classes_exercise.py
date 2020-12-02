class Students:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def grade(self, m, c, p):
        self.m = m
        self.c = c
        self.p = p
        
        average = (self.m + self.c + self.p)/3

        return average 
        
avg_score = Students("Hit", 23)

print(avg_score.grade(12,13,24))

