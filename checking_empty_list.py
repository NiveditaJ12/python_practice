# Program to check if the list is empty

lst = [1,4,3,7]

# Solution 1
if not lst:
    print("The list is empty.")
else:
    print("The list is not empty.")

# Solution 2
if len(lst) == 0:
    print("The list is empty.")
else:
    print("The list is not empty.")

# Solution 3
if lst == []:
    print("The list is empty.")
else:
    print("The list is not empty.")