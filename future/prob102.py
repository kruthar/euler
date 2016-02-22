__author__ = 'kruthar'
'''
Triangle Containment
Three distinct points are plotted at random on a Cartesian plane, for which -1000 <= x, y <= 1000, such that a triangle is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)
X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.
Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing the co-ordinates of one thousand "random" triangles, find the number of triangles for which the interior contains the origin.
NOTE: The first two examples in the file represent the triangles in the example given above.
'''

def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]

f = open('../data/data-prob102.txt')

count = 0

for line in f.readlines():
    points = line.rstrip().split(',')
    A = [int(points[0]), int(points[1])]
    B = [int(points[2]), int(points[3])]
    C = [int(points[4]), int(points[5])]

    vAB = [B[0] - A[0], B[1] - A[1]]
    vBC = [C[0] - B[0], C[1] - B[1]]
    vCA = [A[0] - C[0], A[1] - C[1]]
    vBO = [0 - B[0], 0 - B[1]]
    vCO = [0 - C[0], 0 - C[1]]
    vAO = [0 - A[0], 0 - A[1]]

    signAB = cross(vAB, vBO) < 0
    signBC = cross(vBC, vCO) < 0
    signCA = cross(vCA, vAO) < 0

    if (signAB and signBC and signCA) or (not signAB and not signBC and not signCA):
        count += 1

print count