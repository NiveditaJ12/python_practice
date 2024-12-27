# Program to merge dictionaries

# Solution1: using | operator

def merge_dict1(dict1,dict2):
    return dict1 | dict2

# Solution2: Using ** operator
def merge_dict2(dict1,dict2):
    return {**dict1,**dict2}

# Solution3: Using copy() and update() method
def merge_dict3(dict1,dict2):
    dict2.update(dict1)
    return dict2

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'f': 5, 'w': 7, 'p': 9}
print(merge_dict1(dict1, dict2))
print(merge_dict2(dict1,dict2))
print(merge_dict3(dict1,dict2))