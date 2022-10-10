# Password Generator Project

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
length_letters = int(len(letters) - 1)
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
length_numbers = (len(numbers) - 1)
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
length_symbols = (len(symbols) - 1)

print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
nr_letters = 3
# nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_symbols = 2
# nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_numbers = 2

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

letter_password = ""

for n in letters:
    l = (letters[random.randint(0,length_letters)])
    letter_password +=  l
    if len(letter_password) >= nr_letters:
        break

number_password = ""

for n in numbers:
    l = (numbers[random.randint(0,length_numbers)])
    number_password +=  l
    if len(number_password) >= nr_numbers:
        break

symbols_password = ""

for n in numbers:
    l = (symbols[random.randint(0,length_symbols)])
    symbols_password +=  l
    if len(symbols_password) >= nr_symbols:
        break

print(letter_password + number_password + symbols_password)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

s = letter_password + number_password + symbols_password
random_password = ''.join(random.sample(s,len(s)))
print(random_password)

l = list(s)
random.shuffle(l)
random_password = ''.join(l)
print(random_password)
