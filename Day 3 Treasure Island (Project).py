print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

crossroads = input("Your first choice is whether you'd like to turn 'left' or 'right' on the mysterious path?\n")
if crossroads.lower() == "left":
  swim_wait = input("Congratulations, you made the correct turn!\nNow the path leads to a river, would you like to swim accross the 'river' or 'wait'?\n")
  if swim_wait.lower() == "wait":
    which_door = input("You've definitely made the correct choices.\nIn front of you, there are three different homes all with different colored doors.\nWhich colored door would you like to enter?\n'red', 'blue', or 'yellow'\n")
    if which_door.lower() == "red":
      print("As soon as you opened the door, a huge fireball fell from the sky and killed you!")
    elif which_door.lower() == "blue":
      print("Hungry wolves magically appeared around you and feasted on your body!")
    elif which_door.lower() == "yellow":
      print("You won, you made it to the next dimension!")
    else: print("Game Over")
  else: print("You were attacked by the biggest trout you've ever seen and died!")
else: print("You fell into a hole and died")
