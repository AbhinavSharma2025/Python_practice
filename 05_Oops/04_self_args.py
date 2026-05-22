class Chaicup:
    size=150

    def describe(self):
        return f"A {self.size} ml chai cup"

cup=Chaicup() #object from class
print(cup.describe())#object calling method we dont need to pass arguements as self will reference it
print(Chaicup.describe(cup)) #direct class calling object we need to pass the arguement as object 

cup_two=Chaicup()
cup_two.size=600
print(Chaicup.describe(cup_two))