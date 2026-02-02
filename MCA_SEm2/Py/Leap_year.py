#Leap year

year=int(input("Enter Year"))

if year % 4 == 0:
    print(f"{year} Year is Leap year")
else:
    print(f"{year} year is not a leap year")
