def Sum_of_List(list_values) -> int:

    sum:int = 0
    for i in list_values:
      sum+=i;

    return sum

def main():

  Input_list :list[int] = [12,3,23,4,248,-1,2-88,36]
  print(f"The Sum of the List is {Sum_of_List(Input_list)}")
if __name__ == '__main__':
    main()