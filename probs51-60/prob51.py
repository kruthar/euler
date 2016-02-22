__author__ = 'kruthar'
'''
Prime Digit Replacement
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
'''

from functions import *
from generators import *

limit = 8

for perm in starPerms():
    count = 0
    plist = []
    for i in range(10):
        if i - count > 10 - limit:
            break

        repl = perm.replace("*", str(i))
        if repl[0] != '0' and isPrime(int(repl)):
            count += 1
            plist.append(repl)

    if count == limit:
        found = True
        print plist
        print perm
        plist.sort()
        print plist[0]
        break
