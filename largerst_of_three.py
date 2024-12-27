# Find largest among three numbers.

def largest_num(lst):
    if lst[0] > lst[1]:
        first= lst[0]
        second = lst[1]
    else:
        first = lst[1]
        second = lst[0]
    for i in range(2,len(lst)):
        if lst[i]>first:
            first = lst[i]
            return first
        if lst[i]>second and lst[i] < first:
            return first
    else:
        return first
lst = list(map(int,input("Enter three numbers: ").split(' ')))
print(f'The largest of three numbers is {largest_num(lst)}')