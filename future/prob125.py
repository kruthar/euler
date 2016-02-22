__author__ = 'kruthar'
'''
Palindromic Sums
The palindromic number 595 is interesting because it can be written as the sum of consecutive squares: 6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2.

There are exactly eleven palindromes below one-thousand that can be written as consecutive square sums, and the sum of
these palindromes is 4164. Note that 1 = 0^2 + 1^2 has not been included as this problem is concerned with the squares of positive integers.

Find the sum of all the numbers less than 10^8 that are both palindromic and can be written as the sum of consecutive squares.
'''

palis = dict()

def palindromeFast(digits):
    #if palis.has_key(digits):
    #    return palis[digits]

    results = []
    if digits == 0:
        results.append('')
    elif digits == 1:
        for i in range(10):
            results.append(str(i))
    else:
        for result in palindromeFast(digits - 2):
            for i in range(10):
                si = str(i)
                results.append(si + result + si)
    #palis[digits] = results
    return results

def isSquareSum(n, l, next = -1):
    if n == 0 and l > 1:
        return True

    if next == -1:
        i = 1
        while i ** 2 <= n:
            if isSquareSum(n - i ** 2, l + 1, i + 1):
                return True
            i += 1
        return False
    else:
        if n - next ** 2 >= 0:
            return isSquareSum(n - next ** 2, l + 1, next + 1)

sum = 0
limit = 8
for i in range(1, limit + 1):
    for p in palindromeFast(i):
        if p[0] != '0' and isSquareSum(int(p), 0):
            print p
            sum += int(p)
print sum

