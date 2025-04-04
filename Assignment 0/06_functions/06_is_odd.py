def main():
    for i in range(10):
        if is_odd(i):
            print(f'{i} odd')
        else:
            print(f'{i} even')

def is_odd(value: int):
    return value % 2


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()