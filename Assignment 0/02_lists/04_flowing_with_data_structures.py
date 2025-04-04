def add_three_copies(main_list:list[str] , string_add:str):
    for i in range(3):
        main_list.append(string_add)


def main():
   three_copy_list:list[str]= []
   message = input("Enter message to copy: ")
   add_three_copies(three_copy_list,message)
   print(three_copy_list)


if __name__ == '__main__':
    main()