#each object can have its own entity (namespace) and they todo not overlap
class Chai:
    origin="India"

print(Chai.origin)

Chai.is_hot=True

print(Chai.is_hot)

#creating object from class

masala=Chai()
print(f"Masala is from {masala.origin}")
print(f"is it hot ? :{masala.is_hot}")