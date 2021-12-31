import os

def clear():
  os.system("cls")
  
words = []
score = 0

print("Welcome to the Memory Game!\n")
print("Easy = 5 Words")
print("Medium = 10 Words")
print("Hard = 15 Words")
print("Extreme = 20 Words")
print("Insane = 30 Words")
print("Ludicrous = 50 Words\n")

while True:
  selection = input("Type in your selection: ")
  if selection == "Easy":
    wordAmount = num = 5
    break
  elif selection == "Medium":
    wordAmount = num = 10
    break
  elif selection == "Hard":
    wordAmount = num = 15
    break
  elif selection == "Extreme":
    wordAmount = num = 20
    break
  elif selection == "Insane":
    wordAmount = num = 30
    break
  elif selection == "Ludicrous":
    wordAmount = num = 50
    break
  else:
    print("Invalid selection!")

for x in range(0, wordAmount):
  word = input("Enter a word: ")
  words.append(word)
clear()

for x in range(0, len(words)):
  position = len(words) - num
  print(position)
  response = input("Enter the words you put in before: (type in one words then enter)")
  if response == words[position]:
    score += 1
  num -= 1
print("\nYou got " + str(score) + " points!")
