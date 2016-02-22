__author__ = 'kruthar'
'''
Digit Factorials
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

import math

count = 0
total = 0

while count <= len(str(total)):
    count += 1
    total += math.factorial(9)

print count
print total

result = 0

for a in range(10, total + 1):
    sum = 0
    for digit in str(a):
        sum += math.factorial(int(digit))
    if sum == a:
        print a
        result += a

print result