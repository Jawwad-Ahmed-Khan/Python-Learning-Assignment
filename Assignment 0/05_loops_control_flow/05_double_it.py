def main():
    doubled =  int(input("Enter a Number for Doubled: "))
    while doubled <100:
      print(f"{doubled} doubled is {doubled *2}")
      doubled *=2


if __name__ == '__main__':
    main()