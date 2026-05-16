#[expression for item in iterable if condition]
menu=[
    "Masala Chai",
    "Iced Lemon Tea",
    "Iced peach tea",
    "Ginger chai"
]

iced_tea=[tea for tea in menu if "Iced" in tea]
print(iced_tea)