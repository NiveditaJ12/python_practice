# Program to count vowels in the string

# solution1: Using dictionary

def count_vow(str):
    str = str.casefold()
    vowels = 'aeiou'
    d = {}.fromkeys(vowels,0)

    for i in str:
            if i in d:
                d[i] += 1
    return d

#Solution2: Using dictionary and list comprehension

def count_vow1(str):
    str = str.casefold()
    vowels = 'aeiou'
    d = {key: sum([1 for i in str if i == key]) for key in vowels}
    return d

print(count_vow('hello'))
print(count_vow1('hello'))