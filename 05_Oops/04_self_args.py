class Chaicup:
    size=150

    def describe(self):
        return f"A {self.size} ml chai cup"

cup=Chaicup() #object from class
print(cup.describe())
print(Chaicup.describe(cup)) 

cup_two=Chaicup()
cup_two.size=600
print(Chaicup.describe(cup_two))