def access_element(lst, index):
    """Returns the element at the given index or an error message if out of range."""
    if 0 <= index < len(lst):
        return lst[index]
    else:
        return "Error: Index out of range!"

def modify_element(lst, index, new_value):
    """Replaces an element at the given index with a new value."""
    if 0 <= index < len(lst):
        lst[index] = new_value
        return "Updated List: " + str(lst)
    else:
        return "Error: Index out of range!"

def slice_list(lst, start, end):
    """Returns a sliced portion of the list."""
    if 0 <= start < len(lst) and 0 <= end <= len(lst) and start < end:
        return lst[start:end]
    else:
        return "Error: Invalid slice range!"

def play_game():
    """Text-based game to access, modify, or slice a list."""
    my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']

    while True:
        print("\nChoose an operation:")
        print("1 - Access an element")
        print("2 - Modify an element")
        print("3 - Slice the list")
        print("4 - Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            index = int(input("Enter index to access: "))
            print("Result:", access_element(my_list, index))

        elif choice == '2':
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            print(modify_element(my_list, index, new_value))

        elif choice == '3':
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print("Sliced List:", slice_list(my_list, start, end))

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the game
play_game()
