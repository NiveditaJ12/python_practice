# Check whether the year is leap or not

def leap(year):
    if year%400 == 0 and year%100 == 0:
        return 'The year is leap.'
    elif year % 4 == 0 and year % 100 != 0:
        return 'The year is leap.'
    else:
        return 'The year is not leap.'

year = int(input("Enter the year: "))
print(leap(year))