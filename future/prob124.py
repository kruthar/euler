__author__ = 'kruthar'
'''
Ordered Radicals
The radical of n, rad(n), is the product of the distinct prime factors of n. For example, 504 = 23 x 32 x 7, so rad(504) = 2 x 3 x 7 = 42.

If we calculate rad(n) for 1 <= n <= 10, then sort them on rad(n), and sorting on n if the radical values are equal, we get:

Let E(k) be the kth element in the sorted n column; for example, E(4) = 8 and E(6) = 9.

If rad(n) is sorted for 1 <= n <= 100000, find E(10000).
'''

from functions import *
import heapq

rads = []
limit = 100000
k = 10000

for i in range(1, limit + 1):
    heapq.heappush(rads, (prodList(primeFactors(i)), i))

while k > 1:
    heapq.heappop(rads)
    k -= 1

print heapq.heappop(rads)