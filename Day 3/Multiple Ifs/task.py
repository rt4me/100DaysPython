print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
cost = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
        cost = 5
    elif age <= 18:
        print("Please pay $7.")
        cost = 7
    else:
        print("Please pay $12.")
        cost = 12

    if input("Did you want a picture taken (y/n)?") == 'y':
        cost += 3

    print(f"Total cost will be ${cost}")


else:
    print("Sorry you have to grow taller before you can ride.")
