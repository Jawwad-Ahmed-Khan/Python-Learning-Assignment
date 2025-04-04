def average(input1:float, input2:float):
  return (input1 + input2)/2

def main():
    a= float(input("Enter the first number:"))
    b= float(input("Enter the second number: "))
    print(f"The average of {a} and {b} is {average(a,b)}")


if __name__ == '__main__':
    main()