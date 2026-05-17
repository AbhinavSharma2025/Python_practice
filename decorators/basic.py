from functools import wraps

def my_decorato(func):
    @wraps(func)
    def wrapper():
        print("Before function runs")
        func()
        print("after function runs")
    return wrapper

@my_decorato
def greet():
    print("Hellow from decorators class")

greet()
print(greet.__name__)