'''
You are given a date.  Your task is to find what the day is on that date.
'''

# import calendar

# def find_day(date):
#     # Split the date into day, month, and year
#     day, month, year = map(int, date.split('-'))
    
#     # Use the calendar module to find the day of the week
#     day_of_week = calendar.weekday(year, month, day)
    
#     # Return the name of the day
#     return calendar.day_name[day_of_week]

# # Read the date from input
# date = input()
# # Print the day of the week for the given date
# print(find_day(date))

# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

def find_day(date):
    month, day, year = map(int, date.split())
    
    day_of_week = calendar.weekday(year, month, day)
    
    return calendar.day_name[day_of_week] 

print(find_day(input()).upper())