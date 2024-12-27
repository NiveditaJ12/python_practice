# Python program to generate the prime numbers from 1 to N

def prime_num(num1,num2):
    l = []
    for i in range(num1,num2+1):
        for j in range(2,num2+1):
            if i % j ==0:
                break
        if i==j:
                l.append(i)
        
    return l

print(prime_num(1,100))