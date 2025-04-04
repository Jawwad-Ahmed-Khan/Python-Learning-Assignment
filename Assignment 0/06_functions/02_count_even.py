def count_even(lst):
  count = 0
  for i in lst:
    if i%2==0:
      count+=1
  return count

def main():

  list_of_numbers = []
  ele  = input("Please enter an number of the list or press enter to stop.: ")

  while ele !="":
    list_of_numbers.append(int(ele))
    ele = input("Please enter an number of the list or press enter to stop.: ")

  print(f"{list_of_numbers}  have {count_even(list_of_numbers) } even Numbers")

if __name__ == '__main__':
    main()