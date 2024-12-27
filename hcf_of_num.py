# Find the HCF of two numbers

def hcf_of_nums(num1,num2):
    if num1 > num2:
        smaller = num2
    else:
        smaller = num1
    for i in range(1,smaller+1):
        if (num1%i == 0) and (num2%i == 0):
            hcf = i
    return hcf

def hcf_recurs(num1,num2):
    if num2 == 0:
        return num1
    else:
        return hcf_recurs(num2, num1%num2)
    
print(hcf_of_nums(18,24))
print(hcf_recurs(18,24))