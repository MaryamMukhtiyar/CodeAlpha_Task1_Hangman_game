import random  # Import the random module to use its functions later

# Function to load words from a file and return a list of words
def load_words(filename):
    try:
        with open(filename, "r") as f:
            data = f.readline().strip()
            words = data.split()
            if not words:
                raise ValueError("The file is empty or no valid words found.")
            return words
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Function to display the current state of the guessed word
def display_word(guessed_word):
    print("Current word:", " ".join(guessed_word))

# Function to get a valid guess from the user
def get_guess(already_guessed):
    while True:
        guess = input("Guess a letter: ").upper()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
        elif guess in already_guessed:
            print("You've already guessed that letter. Try again.")
        else:
            return guess

# Function to update the guessed word with the correct guessed letter
def update_guessed_word(word, guessed_word, guess):
    for index in range(len(word)):
        if word[index] == guess:
            guessed_word[index] = guess

# Main game function
def play_game(words, total_chance=6):
    word = random.choice(words).upper()
    guessed_word = ["-"] * len(word)
    already_guessed = set()

    while total_chance > 0:
        display_word(guessed_word)
        guess = get_guess(already_guessed)
        already_guessed.add(guess)

        if guess in word:
            update_guessed_word(word, guessed_word, guess)
            if "".join(guessed_word) == word:
                print("Congratulations, you won!!!")
                break
        else:
            total_chance -= 1
            print("Incorrect guess.")
            print("The remaining chances are:", total_chance)

    else:
        print("Game over. You lose.")
        print("The correct word was:", word)

# Load the words and start the game if words are available
words = load_words("words.txt")
if words:
    play_game(words)
else:
    print("Unable to start the game due to the errors above.")
