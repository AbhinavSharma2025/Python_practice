def train(birth):
    match birth:
        case "sleeper":
            print("enjoi slppere")
        case "ac":
            print("enjoi the ac")
        case"general":
            print("Load lete hai kyu bekar mai")
        case"luxury":
            print("welcome to jannat")

br = input("Enter birth type ac/sleeper/luxury/general : ").lower()
train(br)