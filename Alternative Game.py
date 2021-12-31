import os

def clear():
  os.system("cls")
  
words = []
score = 0

wordAmount = num = int(input("Enter the amount of words you would like to type in and memorise: "))

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
