__author__ = 'kruthar'
'''
Largest Palindrome Product
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

from functions import *

palindrome = 0;

for a in range(100, 1000):
    for b in range(a, 1000):
        prod = a * b
        if isPalindrome(str(prod)) and palindrome < prod:
            palindrome = prod

print palindrome