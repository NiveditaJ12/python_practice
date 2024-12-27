# Program to display calender
import calendar

year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

calender = calendar.month(year,month)
print(calender)