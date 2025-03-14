class User:
    def __init__(self, user_name, user_key): #Initialize Attributes for class. Will be called every time creating an new instance of the class
        print(f"New user being created {user_name}")
        self.user_name = user_name
        self.id = user_key
        self.followers = 0  # Attribute with a default value and not required during initialization
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("tbergin", 1)
user_2 = User("jsmith", 2)

user_1.follow(user_2)
print(f"User 1 following: {user_1.following}; followers: {user_1.followers}")
print(f"User 2 following: {user_2.following}; followers: {user_2.followers}")






class Car:
    def __init__(self):
        self.seats = 5
        self.engine_size = 3
        self.doors = 4

    def enter_race_mode(self):
        self.seats = 2
        self.engine_size = 5

my_car = Car()
my_car.enter_race_mode()

#Class names should be PascalCase (CarCamshaftPulley); not the same as camelCase




