import random


def Binary_search(Arr , start , end , x):
   
   mid = (start + end)//2

   if mid:
      if Arr[mid] == x:
         return f"value at Index : {mid}"
      elif Arr[mid] > x:
         Binary_search(Arr,start,mid,x)
      else:
         Binary_search(Arr,mid+1,end,x)   



my_list = []
for i in range(100):
  my_list.append(random.randint(1,10000))


my_list.sort()

