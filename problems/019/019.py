# Name:     Counting Sundays
# Source:   https://projecteuler.net/problem=19


from datetime import date


print(len([day for year in range(1901, 2001) for month in range(1, 13) if (day := date(year, month, 1)).weekday() == 6]))
