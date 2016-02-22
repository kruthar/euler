__author__ = 'kruthar'
'''
Double-base Palindromes
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

from generators import *
from functions import *

sum = 0

for a in palindrome(1000000):
    if isPalindrome(getBinary(a)):
        sum += a

print sum