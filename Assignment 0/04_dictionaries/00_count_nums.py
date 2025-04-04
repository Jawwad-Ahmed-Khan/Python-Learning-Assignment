# there are multiple way use Count sort To solve find count of number in list or Dictionary
def main():

  count_numbers = {}

  ele = input("Please enter an number of the list or press enter to stop.: ")

  while ele !="":

    if ele in count_numbers:
      count_numbers[ele] += 1
    else:
      count_numbers[ele] = 1

    ele = input("Please enter an number of the list or press enter to stop.: ")


  for i in count_numbers:
    print(f"{i} appears {count_numbers[i]} times")


if __name__ == '__main__':
    main()