minimum_height = "50" # it is work Because Python Follow Lexical. I use String becaue I remove the raise value error because when enter it is empty string not convert into int
def main():

    ele = input("How tall are you? ")

    while ele !="":

      if ele >= minimum_height:
        print("You're tall enough to ride!")
      else:
        print("You're not tall enough to ride, but maybe next year!")

      ele = input("\nHow tall are you? ")




if __name__ == '__main__':
    main()