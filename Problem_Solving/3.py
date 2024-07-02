print("Enter the year:")
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("It's a leap year")
else:
    print("It's NOT a leap year")