# Find the positive, negative or zero number

def pos_neg_num(num):
    if num>0:
        print("NUmber is positive")
    elif num<0:
        print("Number is negative")
    else:
        print("Number is zero")

num = int(input("Enter the number: "))
pos_neg_num(num)