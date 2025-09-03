import random

def choose_word():
    words = ["python", "hangman", "developer", "programming", "code"]
    return random.choice(words)

def display(word, guessed):
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    return display_word

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("🎯 Welcome to Hangman Game 🎯")
    print("Word:", display(word, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("⚠ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Correct guess!")
        else:
            attempts -= 1
            print("❌ Wrong guess! Attempts left:", attempts)

        print("Word:", display(word, guessed_letters))

        if "_" not in display(word, guessed_letters):
            print("🏆 You win! The word was:", word)
            break
    else:
        print("💀 Game over! The word was:", word)

# Run the game
hangman()