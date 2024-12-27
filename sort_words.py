# Program to sort words in alphabetical order

def sort_word(str):
    lst = str.lower().split(" ")
    lst.sort()
    return lst

str = input("Enter the string: ")
print(sort_word(str))

