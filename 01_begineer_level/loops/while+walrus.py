# def tea_temp(temp):
#     while(temp<100):
#         print(f"The tea temp is {temp} currently...")
#         temp=temp+15

# te=int(input("Please enter the current temperature of the tea: "))
# tea_temp(te)


#for else is a thing   else block only runs if the loop didn't break
#walrus operator if(remainder := value % 5 )

flavours=["masala","mint ","green"]
while(flavour :=input("Enter your flavour: ")) not in flavours:
    print(f"The flavour {flavour} you asked for is not available..sorry")