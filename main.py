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

print("You come to a fork in the road...")
choice1 = input("Do you walk left, or right?\n").lower()

if choice1 == "left":
  print("You go left, struggling through the overgrowth before coming to a large lake, there's no way around it")
elif choice1 == "right":
  print("You turn right and there's literally a jaguar right there, you're mincemeat bud.")
  exit("Better luck next time.")
else:
  exit("Come again? You're talking nonsense")

choice2 = input("Do you swim across, or wait a while and see what happens?\nType swim or wait.\n").lower()

if choice2 == "swim":
  quit("Turns out there's a ton of crocodiles in here and you don't even make it 5 metres.")
elif choice2 == "wait":
  print("A little dude turns up in a boat, warning you the lake is full of crocodiles. He'll take you across but you've got to row. You do and it's a ballache, he doesn't shut up the whole time. Better than death tbf.")

choice3 = input("You reach a set of doors, you can only open one. The air smells like death and you heard low animal noises from no specific direction.. \n(Choose Red, Blue or Yellow)\n").lower()

if choice3 == "red":
  quit("The red door contains.. a shit load of snakes! You were bitten and fled, crying, as it swells before your eyes")
elif choice3 == "blue":
  quit("The blue door leads to a room full of juvenile jaguars. Their mother kills you instantly.")
elif choice3 == "yellow":
 print("You found the treasure!")
else:
  quit("You're saying nonsense. You were attacked and killed while jibbering.")
