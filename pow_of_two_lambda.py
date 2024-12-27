# Display power of 2 using lambda function

terms = int(input("Enter the number of terms here: "))
result = list(map(lambda terms: 2**terms, range(terms+1)))
print(result)

for i in range(terms+1):
    print(f'The value of 2 raised to power {i} is {result[i]}')