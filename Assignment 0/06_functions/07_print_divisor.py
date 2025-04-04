def print_divisors(num):
  divisor_list = ""
  print(f"Here The Divisor of {num}")
  for i in range(1,(num//2) + 1 ):
      if num % i == 0 :
        divisor_list += str(i) + " "

  print(f"{divisor_list}{num}")


def main():

  number = int(input("Enter a number: "))
  print_divisors(number)

if __name__ == '__main__':
    main()

