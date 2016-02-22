__author__ = 'kruthar'

'''
The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, forming a chain of two numbers. For this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:

12496 -> 14288 -> 15472 -> 14536 -> 14264 (-> 12496 -> ...)

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element exceeding one million.
'''

from functions import *

divs = dict()
limit = 1000000

for i in range(1, limit):
    m = i * 2
    while m < limit:
        temp = divs.get(m, [])[:]
        temp.append(i)
        divs[m] = temp
        m += i

maxchain = []

for num, divisors in divs.iteritems():
    chain = [num]
    cur = num
    s = sumList(divisors)
    while s not in chain and s > 0:
        chain.append(s)
        cur = s
        s = sumList(divs.get(cur, [-1]))

    if s == num:
        print "CHAIN"
        if len(chain) > len(maxchain):
            maxchain = chain
            print num, chain

print maxchain
print min(maxchain)