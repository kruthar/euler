__author__ = 'kruthar'
'''
Integer Right Triangles
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
'''

max = 0
maxp = 0

for p in range(1, 1001):
    solutions = 0
    for a in range(1, p - 1):
        for b in range(1, p - a):
            c = p - a - b
            if a ** 2 + b ** 2 == c ** 2 and a + b + c == p:
                solutions += 1

    if solutions > max:
        max = solutions
        maxp = p

print maxp