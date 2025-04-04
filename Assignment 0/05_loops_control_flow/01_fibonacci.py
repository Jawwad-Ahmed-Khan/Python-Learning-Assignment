def main():
 start = 0
 end = 1

 fib_string = "0 1"

 sum = start + end

 while sum <10000:
   fib_string += " " + str(sum)
   start = end
   end = sum
   sum = start + end

 print(fib_string)

if __name__ == '__main__':
    main()