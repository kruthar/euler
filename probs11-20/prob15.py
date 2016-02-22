__author__ = 'kruthar'
'''
Lattice Paths
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?
'''

nodes = dict()

def lattice(width, height, x, y):
    if nodes.has_key("%d %d" % (x, y)):
        return nodes["%d %d" % (x, y)]

    if width == x or height == y:
        return 1

    paths = 0

    if x == y:
        paths += 2 * lattice(width, height, x + 1, y)
    else:
        if x < width:
            paths += lattice(width, height, x + 1, y)

        if y < height:
            paths += lattice(width, height, x, y + 1)

    nodes["%d %d" % (x, y)] = paths
    return paths

print lattice(20, 20, 0, 0)