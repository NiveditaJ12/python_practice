# Find the numbers in the given range divisible by another number

num = int(input('Enter the number: '))
lst = []
for i in range(1,101):
    if i%num==0:
        lst.append(i)
print(lst)

# using filter and lambda
result = list(filter(lambda i: i%num==0, range(1,101) ))
print(result)