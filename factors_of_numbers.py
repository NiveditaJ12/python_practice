# Find the factors of a number

def factors_of_num(num):
    lst = []
    for i in range(1,num+1):
        if num%i==0:
            lst.append(i)
    return lst

def factors_recurse(num,i):
    
     if i<=num:
         if num%i == 0:
             print(i,end = " ")
         
         return factors_recurse(num, i+1)
         
num = int(input("Enter the number: "))
print(factors_recurse(num,1))