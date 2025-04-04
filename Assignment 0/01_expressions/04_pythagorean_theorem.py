import math

def main():

  length =  float(input("Enter the Value of Length AB: "))
  width = float(input("Enter the value of Width AC: "))

  Hypotenious = math.sqrt(length**2 + width**2)

  print(f"\nThe Length of AB (Length) = {length}\n")
  print(f"The Length of AC (width) = {width}\n")
  print(f"The Length of BC (Hypotenious) = {round(Hypotenious,31)}\n")

if __name__ == "__main__":
  main()