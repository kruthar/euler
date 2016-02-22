__author__ = 'kruthar'
'''
Square remainders
Let r be the remainder when (a-1)^n + (a+1)^n is divided by a^2.

For example, if a = 7 and n = 3, then r = 42: 63 + 83 = 728 = 42 mod 49. And as n varies, so too will r, but for a = 7 it turns out that rmax = 42.

For 3 <= a <= 1000, find sig(rmax).
'''

def repeats(l):
    if len(l) % 2 != 0:
        return False

    half = len(l) / 2
    for i in range(half):
        if l[i] != l[half + i]:
            return False

    return True

def sqrem(a):
    n = 1
    rems = []
    while True:
        total = ((a - 1) ** n + (a + 1) ** n)
        rems.append(int(total % a ** 2))
        if repeats(rems):
            return max(rems)

        n += 1

sum = 0
for i in range(3, 1001):
    print i
    sum += sqrem(i)

print sum