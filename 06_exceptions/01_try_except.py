chai_menu= {"masala":30,"ginger":40}

try:
    chai_menu["elaichi"]

except KeyError:
    print("The key you are trying to access is not valid")

print("Hellow chai code")