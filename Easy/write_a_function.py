'''
Given a year, determine whether it is a leap year. If it is a leap year, return True; otherwise, return False.
'''
def is_leap_year(year):
    # Return True if the year is a leap year, otherwise return False
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


year = int(input())
print(is_leap_year(year))