def odd_even(num):
    return 'Even' if num%2==0 else 'Odd'

num = int(input("Enter the number to be checked: "))
print(odd_even(num))