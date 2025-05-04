#Password Generator Project
import random

class PassGen:
    letters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    numbers = list('0123456789')
    symbols = list('!#$%&()*+')


    #This classmethod allow usage of the Class Variable above.
    @classmethod
    def generate_password(cls):
        nr_letters = random.randint(8, 10)
        nr_symbols = random.randint(2, 4)
        nr_numbers = random.randint(2, 4)

        # cls stands for "class" — it's just like self, but for the class itself instead of an instance.
        # @classmethod above means the method belongs to the class (PassGen), not to an object created from it.
        # cls is a reference to the class (PassGen), allowing you to access class variables like cls.letters, cls.numbers, etc.
        password_list = (
            [random.choice(cls.letters) for letter in range(nr_letters)] +  # List of randome letters
            [random.choice(cls.symbols) for symbol in range(nr_symbols)] +  # List of random symbols
            [random.choice(cls.numbers) for number in range(nr_numbers)]    # List of random numbers
        )
    
            # Replaced the below with List Comprehension above
        # for char in range(nr_letters):
        #     password_list.append(random.choice(letters))

        # for char in range(nr_symbols):
        #     password_list += random.choice(symbols)

        # for char in range(nr_numbers):
        #     password_list += random.choice(numbers)

        random.shuffle(password_list)

        # password = ""
        # for char in password_list:
        #     password += char
        
        # Shorter way of doing the above
        # Join items in a list into one string using .join method.
        # You can also replace the "" with something like "|" to put a pipe between each list item.
        password = "".join(password_list)

        print(f"Your password is: {password}")
        return password



if __name__ == "__main__":
    PassGen.generate_password()