def snack(str):
    if(str=="samosa" or str=="Samosa"):
        pritn("Available")
    elif(str=="cookies" or str=="Cookies"):
        print("Available")
    else:
        print(f"The Item {str} you asked for is not available ")

sna=input("Please enter the snack you want->  ")
snack(sna)