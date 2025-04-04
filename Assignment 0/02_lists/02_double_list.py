def Double_of_List(list_values) -> list[int]:

   return [i*2 for i in list_values]

def main():

  Input_list :list[int] = [12,3,23,4,248,-1,2-88,36]
  print(f"The Original List is {Input_list}\n")
  Input_list = Double_of_List(Input_list)
  print(f"The Double of the List is {Input_list}")

if __name__ == '__main__':
    main()