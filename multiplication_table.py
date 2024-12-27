# Print the multiplication table
#Using for loop
def multi_table(num):
    for i in range(1,11):
        ans = i*num
        print(f'{num} * {i} = {ans}')

# Using while loop
def mult_table(num):
    i=1
    while i<=10:
        ans = num * i
        print(f'{num} * {i} = {ans}')
        i+=1

num = int(input("Enter the number: "))
mult_table(num)