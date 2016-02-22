__author__ = 'kruthar'
'''
Counting Rectangles
By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:

Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.
'''

def getRectangles(x, y):
    count = 0
    for a in range(1, x + 1):
        for b in range(1, y + 1):
            count += (x - a + 1) * (y - b + 1)
    return count

x = 1
y = 1
closest = 0
cx = 0
cy = 0
limit = 2000000
diff = 1


# Find the maximum dimensions with one side being 1
while getRectangles(x, y) < limit:
    x += 1

while x >= 1:
    recs = getRectangles(x, y)
    if recs < limit:
        break
    dx = x
    while recs > limit:
        recs = getRectangles(dx, y)
        if abs(limit - recs) < closest or closest == 0:
            closest = abs(limit - recs)
            cx = dx
            cy = y
        dx -= 1

    y += 1
    x -= diff
    diff = x - dx

print closest
print str(cx) + ' * ' + str(cy) + ' = ' + str(cx * cy)


