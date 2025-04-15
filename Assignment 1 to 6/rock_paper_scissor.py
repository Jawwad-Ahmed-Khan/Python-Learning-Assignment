import random

# Map shorthand to full names and emojis
choices = {
    "r": ("rock", "🪨"),
    "p": ("paper", "📄"),
    "s": ("scissors", "✂️")
}

# Get player choice
player_input = input("Enter your choice (r for rock, p for paper, s for scissors): ").lower()

# Validate input
if player_input not in choices:
    print("Invalid input! Please enter r, p, or s.")
else:
    # Random computer choice
    computer_input = random.choice(list(choices.keys()))

    # Get full names and emojis
    player_choice, player_emoji = choices[player_input]
    computer_choice, computer_emoji = choices[computer_input]

    # Show choices
    print(f"\nYou chose: {player_choice} {player_emoji}")
    print(f"Computer chose: {computer_choice} {computer_emoji}")

    # Determine result
    if player_input == computer_input:
        print("It's a tie!")
    elif (player_input == "r" and computer_input == "s") or \
         (player_input == "s" and computer_input == "p") or \
         (player_input == "p" and computer_input == "r"):
        print("You win! 🎉")
    else:
        print("Computer wins! 🤖")
