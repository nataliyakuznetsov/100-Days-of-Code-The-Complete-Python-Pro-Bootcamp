import random
from password_info import letters, numbers, symbols

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

# creating a random list of letters
for letter in range(0, nr_letters):
   password_list.append(random.choice(letters))

# creating a random list of numbers
for number in range(0, nr_numbers):
   password_list.append(random.choice(numbers))

# creating a random list of symbols
for symbol in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

# to shuffle all items in the list
    random.shuffle(password_list)

password = ""
# creating a new string
for char in password_list:
    password += char
# output
print(f"Your password is: {password}")
