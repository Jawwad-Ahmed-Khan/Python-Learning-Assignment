def print_multiple(string, times):
  for i in range(times):
    print(string)

def main():
    message = input("Please type a message: ")
    times = int(input("Enter a number of times: "))
    print_multiple(message, times)

if __name__ == '__main__':
    main()