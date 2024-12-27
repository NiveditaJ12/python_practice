def degree_faran(temp):
    ans = (9*(temp)/5)+32
    return ans

temp = float(input("Enter the temperature: "))
print(degree_faran(temp))