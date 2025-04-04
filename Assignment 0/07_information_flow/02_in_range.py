def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    if n >= low and n <= high:
        return True
    return False


def main():
    # Example test cases
    test_values = [(5, 1, 10), (0, 1, 10), (10, 1, 10), (15, 1, 10)]
    for n, low, high in test_values:
        result = in_range(n, low, high)
        print(f"{n} in range({low}, {high})? {result}")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()