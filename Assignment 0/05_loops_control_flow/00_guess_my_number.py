import random
def main():
  my_number = random.randint(0,100)

  try:
    guess = int(input("I am thinking of a number between 0 and 99... Enter a guess: "))

    if guess < my_number:
      print("Your Guess is too Low")
    else:
      print("Your Guess is too High")

    while guess != my_number:
      guess = int(input("Enter New Number: "))
      if guess < my_number:
         print("Your Guess is too Low")
      elif guess > my_number:
        print("Your Guess is too High")
      else:
        print(f"Congrats! The number was: {guess}")
  except:
    print("You provide wrong input")




if __name__ == '__main__':
    main()