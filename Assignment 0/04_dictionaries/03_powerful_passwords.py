import hashlib

def Generate_Hash():
  pawd = input("Enter Your Password: ")

  return hashlib.sha256(pawd.encode()).hexdigest()

def Login(my_dic):
  print("\n\n------------------ | Login To Website | ---------------------------\n\n")
  email = input("Enter Your Email: ")
  if email in my_dic:
    password = Generate_Hash()
    if my_dic[email] == password:
      print("You Are Logged IN")
    else:
      print("You Enter the Wrong Password")
  else:
    print("This Email is Not Exist")

def main():

   Mypasswords = {

   }

   gmail = input("Enter the Email: ")
   while gmail !="":
     password = Generate_Hash()
     Mypasswords[gmail] = password
     gmail = input("Enter the Email: ")

   Login(Mypasswords)

if __name__ == '__main__':
    main()
