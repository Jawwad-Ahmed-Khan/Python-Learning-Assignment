import os
import string

path = "C:/Users/jawad/Downloads/"

i = 1
for file in os.listdir(path):
 
  try:
      file_type = file.split(".")[1]
      print(file_type)
      if file_type in ["jpeg","png","jpg"]:
           my_dest = path + "img_" + str(i) +"."+ file_type
           my_source = path + file
           os.rename(my_source,my_dest)
           i+=1
  except:
     print(f"{file} have not type")
    

    
