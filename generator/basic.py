#generator fun are for memory optimization, lazy evaluation,you don't want the result immediately 


def ser_chai():
    yield "cup 1: Masala Chai"
    yield "cup 2: Ginger Chai"
    yield "cup 3: Elaichi Chai"

stall=ser_chai() #stall is just a reference to ser_chai()fun memory

# for cup in stall:
#     print(cup)


def get_chai_list():
    return["Cup 1","Cup 2","cup 3"]

#generator Fun

def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai=get_chai_gen()
print(next(chai))
print(next(chai))
print(next(chai))
