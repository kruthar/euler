__author__ = 'kruthar'
'''
Champernowne's Constant
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
'''

fraction = ''
count = 1

while len(fraction) < 1000000:
    fraction += str(count)
    count += 1

print int(fraction[0]) * int(fraction[9]) * int(fraction[99]) * int(fraction[999]) * int(fraction[9999]) * int(fraction[99999]) * int(fraction[999999])