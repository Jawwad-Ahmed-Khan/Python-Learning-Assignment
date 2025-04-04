def main():
  Divident = int(input("Please enter an integer to be divided: "))
  Divisor = int(input("\nPlease enter an integer to divide by: "))

  print(f"\nThe result of this division is {Divident//Divisor} with a remainder of {Divident % Divisor}")

if __name__ == "__main__":
  main()