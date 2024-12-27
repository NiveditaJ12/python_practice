# Program to access index of list using for loop
# solution1- using enumerate
lst = ['a','b','c','d']

# for index,value in enumerate(lst,1):
#     print(index,'-', value)

#Solution2- without using enumerate
for i in range(len(lst)):
    print(i,'-',lst[i])