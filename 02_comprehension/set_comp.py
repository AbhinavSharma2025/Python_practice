#{expression for item in iterable if condition}
#usually used for finding unique item
favourite_chai=[
    "Masala Chai",
    "Green Tea",
    "Masala Chai",
    "Lemon Tea","Green Tea",
    "Elaichi Chai"
]

unique_chai={chai for chai in favourite_chai }
print(unique_chai)

recipes={
    "Masala hai":["ginger","cardmom","clove"],
    "Elaichi hai":["cardmom","milk"],
    "spicy Chai":["ginger","black pepper","clove"],
}

unique_spice={spice for ingredients in recipes.values() for spice in ingredients}
print(unique_spice) 