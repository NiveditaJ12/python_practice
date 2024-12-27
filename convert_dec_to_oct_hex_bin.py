# Convert decimal to octal, hex and binary

# decimal = int(input("Enter the number here: "))
# print("The conversion of decimal number", decimal, "is ")
# print(bin(decimal), "in binary.")
# print(oct(decimal), "in octal")
# print(hex(decimal), "in hexadecimal")

# Convert decimal to binary using recursion
def recurse_dec_bin(num):
    if num>1:
        recurse_dec_bin(num//2)
    print(num%2, end="")

recurse_dec_bin(15)