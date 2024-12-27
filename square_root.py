# Find and calculate square root

def square_root(num):
   for i in range(1,num+1):
      if num//i==i:
         return i
      
def sqr_rt_fun(num):
    from math import sqrt
    return sqrt(num)

num = int(input("Enter the number for which square root needs to be found: "))
print(square_root(num))
print(sqr_rt_fun(num))
