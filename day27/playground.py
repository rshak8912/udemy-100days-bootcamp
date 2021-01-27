def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

#print(add(3,5,6,2,1,7,4,3))

def calculate(n, **kwargs):
    print(kwargs)
    print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **a):
        self.make = a["make"]
        self.model = a["model"]
my_car = Car(make="ssangyong", model="lexton")
print(my_car.model)