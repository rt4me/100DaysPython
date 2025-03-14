
# Unlimited Positional Arguments
# Doesn't necessarily have to be named *args.
# Could be *numbers. The asterisk is the important character
def add(*args):
    # ttl = 0
    # for n in args:
    #     ttl += n
    # return ttl
    return sum(args)

print(add(2,2,5))


def calculate(n, **kwargs):
    print(kwargs)  # outputs {'add': 3, 'multiply': 5}
    for key, value in kwargs.items():
        print(key) #outputs add, then multiply
        print(value) # outputs 3, then 5
    print(kwargs["add"]) # outputs 3
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n) # output 35

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self,**kw):
        self.make = kw["make"]
        #self.model = kw["model"]
        self.model = kw.get("model") # similar to the line above, but if a value isn't provided then it will just set to none instead of causing an error.


my_car = Car(make="Ford")
print(my_car.make)
print(my_car.model)













