#ternary operator
def order(amount):
    delivery_Fee = 0 if amount>300 else 30
    print(f"deliver fee is {delivery_Fee}")

amt=int(input("Enter the total amount gng :"))
order(amt)