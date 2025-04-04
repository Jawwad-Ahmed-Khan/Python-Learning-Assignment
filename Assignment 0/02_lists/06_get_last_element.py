def get_last_element(lst):
  try:
    print(lst[-1])
  except:
    print("You Provide Empty List")

def main():
    lst1 :list= [1,2,3]
    lst2 :list= []
    print("Pass List 1:\n")
    get_last_element(lst1)
    print("\nPass List 2:\n")
    get_last_element(lst2)

if __name__ == '__main__':
    main()