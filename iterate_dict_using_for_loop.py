# Program to iterate over dictionaries using for loop

d = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e'}

# Solution1: using .items()
for key,val in d.items():
    print(key,val)
print()
# Solution2: using keys() and values()

for key in d.keys():
    print(key,d[key])
print()

for key in d:
    print(key)
print()

for value in d.values():
    print(value)
