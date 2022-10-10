# Password Generator Project

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
length_letters = int(len(letters) - 1)
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
length_numbers = (len(numbers) - 1)
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
length_symbols = (len(symbols) - 1)

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_letters = 3
nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_symbols = 2
nr_numbers = int(input(f"How many numbers would you like?\n"))
# nr_numbers = 2

password = ""
count = 0
for char in range(1, nr_letters + 1):
    password += random.choice(letters)
    print(count + 1)

for symbol in range(1, nr_symbols + 1):
    password += random.choice(symbols)

for number in range(1, nr_numbers + 1):
    password += random.choice(numbers)

print(password)

l = list(password)
random.shuffle(l)
random_password = ''.join(l)
print(random_password)