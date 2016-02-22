__author__ = 'kruthar'
'''
The points P (x1, y1) and Q (x2, y2) are plotted at integer co-ordinates and are joined to the origin, O(0,0), to form tOPQ.


There are exactly fourteen triangles containing a right angle that can be formed when each co-ordinate lies between 0 and 2 inclusive; that is,
0 <= x1, y1, x2, y2 <= 2.


Given that 0 <= x1, y1, x2, y2 <= 50, how many right triangles can be formed?
'''
x = 50
y = 50
count = 0

for x1 in range(x + 1):
    for y1 in range(1, y + 1):
        for x2 in range(x1, x + 1):
            for y2 in range(y1 + 1):
                a = x1 ** 2 + y1 ** 2
                b = x2 ** 2 + y2 ** 2
                c = abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2
                points = [a, b, c]
                hypo = max(points)
                points.remove(hypo)
                if sum(points) == hypo and min(a, b, c) > 0:
                    count += 1
                    print x1, y1, x2, y2

print count