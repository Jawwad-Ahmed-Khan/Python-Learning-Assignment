import random
def main():

    print("Print 10 random numbers in the range 1 to 100.\n")
    ten_random_numbers = []
    for i in range(10):
      ten_random_numbers.append(random.randint(1,100))
    print(ten_random_numbers)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()