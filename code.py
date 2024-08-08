import random
f= open("words.txt","r")
data= f.readline()
words= data.split()
word = random.choice(words)
total_chance = 6
guessed_word = "-"*len(word)
while total_chance!=0:
  print(guessed_word)

  letter = input ("Guess a letter:").upper()
  if letter in word:
      for index in range (len(word)):
          if word[index]==letter:
            guessed_word=guessed_word[:index]+letter+guessed_word[index+1:]
            #print(guessed_word)
      if guessed_word== word:
        print("Congratulations you won!!!")
        break
  else:
    total_chance-= 1
    print("Incorrect guess")
    print("The remaning chance are:", total_chance)
else:
  print ("Game over")
  print ("You lose")
  print ("All the chances are exhausted")
print ("The correct word is:", word)
