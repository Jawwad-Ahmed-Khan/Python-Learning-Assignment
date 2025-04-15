import random

# List of words to choose from
word_list = [
    "apple", "banana", "grapes", "orange", "strawberry",
    "mango", "cherry", "watermelon", "pineapple", "blueberry"
]

# Choose a random word
word = random.choice(word_list)
word_letters = set(word)
guessed_letters = set()
wrong_guesses = 0
max_guesses = 6

print("🎮 Welcome to Hangman!")
print("_ " * len(word))

# Game loop
while wrong_guesses < max_guesses and word_letters:
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in word_letters:
        word_letters.remove(guess)
        print("✅ Good guess!")
    else:
        wrong_guesses += 1
        print(f"❌ Wrong guess! You have {max_guesses - wrong_guesses} tries left.")

    # Show current state of the word
    display_word = [letter if letter in guessed_letters else "_" for letter in word]
    print(" ".join(display_word))

# End of game
if not word_letters:
    print(f"\n🎉 You won! The word was '{word}'.")
else:
    print(f"\n💀 You lost. The word was '{word}'.")
