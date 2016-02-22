__author__ = 'kruthar'
'''
Counting Sundays
You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September, April, June and November.
    All the rest have thirty-one, Saving February alone, which has twenty-eight, rain or shine. And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

day = 1
month = 1
year = 1900
dow = 1 # 1 = Monday

daysInMonth = {1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6: 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}

count = 0

while year < 2001:
    if dow == 7 and day == 1 and year >= 1901:
        count += 1

    expected = daysInMonth[month]

    if month == 2 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        expected += 1

    day += 1

    if day > expected:
        day = 1
        month += 1

        if month > 12:
            month = 1
            year += 1

    dow += 1

    if dow > 7:
        dow = 1

print count

