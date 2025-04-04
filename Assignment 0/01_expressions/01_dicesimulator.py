import random

def Dice_Role():
  Dice1 = random.randint(1,6)
  Dice2 = random.randint(1,6)

  print(f"Dice 1: {Dice1}")
  print(f"Dice 2: {Dice2}")
  print(f"Total: {Dice1 + Dice2}\n")

def main():

 for i in range(3):
  print(f"----------| Role {i+1} | ----------- \n")
  Dice_Role()


if __name__ == '__main__':
    main()