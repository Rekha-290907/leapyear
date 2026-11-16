import sys

def leap(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

year = int(sys.argv[1])

print(leap(year))