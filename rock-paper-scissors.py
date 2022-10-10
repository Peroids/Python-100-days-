rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

lst_choice = [rock,paper,scissors]

print(lst_choice[choice])

import random

comp_choice = int(random.randint(0,2))

print(f"Computer chose")

print(lst_choice[comp_choice])

if choice == 0:
    if comp_choice == 2:
        print("You win")
    elif comp_choice == 1:
        print("You lose")
    elif comp_choice == 0:
        print("You tied")
    else:
        print("Invalid Choice")

if choice == 1:
    if comp_choice == 2:
        print("You lose")
    elif comp_choice == 1:
        print("You tied")
    elif comp_choice == 0:
        print("You win")
    else:
        print("Invalid Choice")

if choice == 2:
    if comp_choice == 2:
        print("You tied")
    elif comp_choice == 1:
        print("You win")
    elif comp_choice == 0:
        print("You lose")
    else:
        print("Invalid Choice")