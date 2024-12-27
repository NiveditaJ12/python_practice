# Python code for multiple exception handling

string = input("Enter the string here: ")

try:
    num = int(input("Enter the number here: "))
    print(string + num)
except (TypeError,ValueError) as error:
    print(error)