def teacup(size):
    if(size=="small"):
        print("Here comes your small tea")
    elif(size=="medium"):
        print("Here comes you medium tea")
    elif(size=="large"):
        print("Cannot stop ya can I..here is your large tea")
    else:
        print("Behave yourself and selcet from the provided menu ")


size=input("Enter the size of cup you want gang : ").lower()
teacup(size)