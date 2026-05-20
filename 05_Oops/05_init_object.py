class ChaiOrder():

    def __init__(self,type_,size):
        self.type=type_
        self.size=size

    def summry(self):
        return f"{self.size} ml of {self.type} chai" 


order=ChaiOrder("Masala",1200)
print(order.summry())

order_two=ChaiOrder("Ginger",200)
print(order_two.summry())