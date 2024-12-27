# Find whether the string is palindrome or not

def pal_str(str1):
    new_str = str1.lower()
    return True if new_str == new_str[::-1] else False

# using for loop
def pal_str_for(str1):
    n=len(str1)
    new_str = str1.lower()
    for i in range(n):
        if new_str[i] == new_str[n-i-1]:
            return True
        else:
            return False

# By using in-built functions-reversed and join
def pal_str_fun(str1):
    new_str = str1.lower()
    new_lst = list(reversed(new_str))
    mod_str = "".join(new_lst) 
    return True if mod_str==new_str else False

# By using while loop
def pal_str_while(str1):
    new_str = str1.lower()
    n = len(new_str)
    i=0
    while i<n:
        if new_str[i] == new_str[n-i-1]:
            i += 1
            continue
        else:
            return False
    return True
            
# print(pal_str("Danoid"))
# print(pal_str_for("Dabkhk"))
# print(pal_str_fun("Daad"))
print(pal_str_while("Dad"))
