
def main():
  my_list =[]

  blue = "\033[94m"  # ANSI code for blue text
  reset = "\033[0m"  # ANSI code to reset text color

  ele = input(f"{blue}Please enter an element of the list or press enter to stop.:{reset} ")

  while ele != "":
    my_list.append(ele)
    ele = input(f"{blue}Please enter an element of the list or press enter to stop.:{reset} ")


  print(f"\n\nThe List is {my_list}")



if __name__ == '__main__':
    main()