Max_lenth = 5

def shorter(temp_lsit):
  while len(temp_lsit) > Max_lenth:
   pop_element = temp_lsit.pop()
   print(f"The Pop element : {pop_element}")
def main():
    my_list = []

    ele = input("Please enter an element of the list or press enter to stop.: ")

    while ele !="":
      my_list.append(ele)
      ele = input("Please enter an element of the list or press enter to stop.: ")

    if (len(my_list) > Max_lenth):
      shorter(my_list)

    print(f"The List is {my_list}")

if __name__ == '__main__':
    main()