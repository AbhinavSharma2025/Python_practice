def process_order(item,quantity):
    try:
        price={"masala":20}[item]  #fetches matching value for key(item) from dict 
        cost=price * quantity
        print(f"total cost is {cost}")

    except KeyError:
        print("Sorry that chai is not on meny")
    except TypeError:
        print("Quantity must be a number")

process_order("ginger",2)
process_order("masala","two")
