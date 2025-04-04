def Feet_to_Inches(feet_value:float)->float:
  return feet_value * 12

def main():

  user_input = float(input("Enter the Value of Feet:  "))
  print(f"Feet {user_input} into Inches is {Feet_to_Inches(user_input)}")

if __name__ == "__main__":
  main()