# Find whether the number is odd or even.

def odd_or_even(num):
    if num%2==0:
        return 'The number is even'
    else:
        return 'The number is odd'

while True:
    num = int(input('Enter the number: '))
    print(odd_or_even(num))

