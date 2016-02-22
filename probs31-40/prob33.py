__author__ = 'kruthar'
'''
Digit Canceling Fractions
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''

from decimal import *

numer = 1
denom = 1

for a in range(10, 99):
    for b in range(a + 1, 100):
        for check in range(0, 10):
            stra = str(a)
            strb = str(b)
            strcheck = str(check)
            if strcheck == stra[0] and strcheck == strb[0] and stra[1] != '0' and strb[1] != '0' and Decimal(a) / Decimal(b) == Decimal(stra[1]) / Decimal(strb[1]):
                numer *= int(stra[1])
                denom *= int(strb[1])

            if strcheck == stra[0] and strcheck == strb[1] and stra[1] != '0' and strb[0] != '0' and Decimal(a) / Decimal(b) == Decimal(stra[1]) / Decimal(strb[0]):
                numer *= int(stra[1])
                denom *= int(strb[0])

            if strcheck == stra[1] and strcheck == strb[0] and stra[0] != '0' and strb[1] != '0' and Decimal(a) / Decimal(b) == Decimal(stra[0]) / Decimal(strb[1]):
                numer *= int(stra[0])
                denom *= int(strb[1])

            # Trivial
            #if strcheck == stra[1] and strcheck == strb[1] and stra[0] != '0' and strb[0] != '0' and Decimal(a) / Decimal(b) == Decimal(stra[0]) / Decimal(strb[0]):
            #    print '%d / %d = %f' % (a, b, Decimal(a) / Decimal(b))
            #    print '%s / %s = %f' % (stra[0], strb[0], Decimal(stra[0]) / Decimal(strb[0]))

print numer
print denom