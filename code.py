import random  # Import the random module to use its functions later

# Open the file "words.txt" in read mode and assign it to variable 'f'
f = open("words.txt", "r")

# Read the first line from the file and store it in the variable 'data'
data = f.readline()

# Split the line into individual words and store them in a list called 'words'
words = data.split()

# Randomly select a word from the 'words' list and store it in the variable 'word'
word = random.choice(words)

# Set the total number of chances the player has to guess the word
total_chance = 6

# Initialize 'guessed_word' with dashes ("-"), the same length as the word to guess
guessed_word = "-" * len(word)

# Begin a while loop that continues until the player runs out of chances
while total_chance != 0:
    # Print the current state of the guessed word (e.g., "--L--" if the word is "HELLO")
    print(guessed_word)

    # Ask the player to guess a letter and convert it to uppercase
    letter = input("Guess a letter: ").upper()

    # Check if the guessed letter is in the word
    if letter in word:
        # If the letter is in the word, loop through each letter in the word
        for index in range(len(word)):
            # If the guessed letter matches the current letter in the word
            if word[index] == letter:
                # Update the guessed word with the correct letter at the appropriate position
                guessed_word = guessed_word[:index] + letter + guessed_word[index + 1:]
        
        # If the guessed word now matches the original word, the player has won
        if guessed_word == word:
            print("Congratulations you won!!!")
            break  # Exit the loop as the game is over

    else:
        # If the guessed letter is not in the word, decrease the total chances by 1
        total_chance -= 1
        print("Incorrect guess")
        print("The remaining chances are:", total_chance)

# If the player runs out of chances, the loop exits and the game is over
else:
    print("Game over")
    print("You lose")
    print("All the chances are exhausted")

# Print the correct word at the end of the game
print("The correct word is:", word)

