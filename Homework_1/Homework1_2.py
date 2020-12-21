year = int(input("Enter the year: "))
if (year >= 1) and (year <= 2021):
    if year % 100 == 0:
        print(year//100)
    else:
        print((year//100)+1)
