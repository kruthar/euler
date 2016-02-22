__author__ = 'kruthar'
'''
Digit Fifth Powers
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

count = 0
total = 0

while len(str(total)) >= count:
    total += 9 ** 5
    count += 1

def fifthPowerSum(num):
    total = 0
    for a in num:
        total += int(a) ** 5
    return total

sum = 0

for a in range(10, total):
    if a == fifthPowerSum(str(a)):
        print a
        sum += a
print sum