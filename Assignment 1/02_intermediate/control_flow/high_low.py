# High and Low Game

import random

NUM_ROUNDS = 3

def generate_number():
  a = random.randint(1,100)
  b = random.randint(1,100)

  return a,b

def Performance_measure(score):

  if score== NUM_ROUNDS:
          print(f"Your score is now {score}")
          print("Wow! You played perfectly!")
  elif score >= NUM_ROUNDS  // 2:
          print(f"Your score is now {score}")
          print("Good job, you played really well!")
  else:
          print(f"Your score is now {score}")
          print("Better luck next time!")


def main():
    print("Welcome to the High-Low Game!")
    print("-----------------------------")

    score = 0

    for i in range(NUM_ROUNDS):
      print(f"\nRound {i+1}")
      my_number, computer_number = generate_number()
      print(f"Your Number is {my_number}")
      guess = input("Do you think your number is higher or lower than the computer's?: ")

      if (guess == "higher" and my_number > computer_number) or (guess == "lower" and my_number<computer_number):
          print(f"You were right! The computer's number was {computer_number}")
          score += 1
          print(f"Your score is now {score}\n")
      else:
          print(f"Aww, that's incorrect. The computer's number was {computer_number}")
          print(f"Your score is now {score}\n")


    Performance_measure(score)


if __name__ == '__main__':
    main()