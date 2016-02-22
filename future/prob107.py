__author__ = 'kruthar'
'''
Minimal Network
The following undirected network consists of seven vertices and twelve edges with a total weight of 243.


The same network can be represented by the matrix below.

    	A	B	C	D	E	F	G
A	-	16	12	21	-	-	-
B	16	-	-	17	20	-	-
C	12	-	-	28	-	31	-
D	21	17	28	-	18	19	23
E	-	20	-	18	-	-	11
F	-	-	31	19	-	-	27
G	-	-	-	23	11	27	-
However, it is possible to optimise the network by removing some edges and still ensure that all points on the network
remain connected. The network which achieves the maximum saving is shown below. It has a weight of 93, representing a
saving of 243 - 93 = 150 from the original network.


Using network.txt (right click and 'Save Link/Target As...'), a 6K text file containing a network with forty vertices, and given in matrix form, find the maximum saving which can be achieved by removing redundant edges whilst ensuring that the network remains connected.
'''

import heapq

class graph():
    def __init__(self):
        self.g = dict()

    def graphweight(self):
        total = 0
        for node, connections in self.g.iteritems():
            for connection, weight in connections.iteritems():
                total += weight
        return total / 2

    def nodes(self):
        return self.g.keys()

    def getweight(self, a, b):
        return self.g[a][b]

    def hasNode(self, node):
        return self.g.has_key(node)

    def addNode(self, node):
        self.g[node] = dict()

    def connect(self, a, b, weight):
        self.g[a][b] = weight
        self.g[b][a] = weight

    def printGraph(self):
        for node, connections in self.g.iteritems():
            for connection, weight in connections.iteritems():
                print node, '->', connection, ':', weight

    def shortestPath(self, a, b):
        seen = [a]
        q = []
        for node, weight in self.g[a].iteritems():
            heapq.heappush(q, (weight, [a, node]))
            seen.append(node)


        while True:
            cost, current = heapq.heappop(q)

            if current[-1] == b:
                return current, cost
            else:
                for node, weight in self.g[current[-1]].iteritems():
                    if node not in seen:
                        seen.append(node)
                        heapq.heappush(q, (cost + weight, current + [node]))

    def mst(self):
        components = dict()
        mstree = graph()

        seen = []
        for node, comp in components.iteritems():
            if node not in seen:
                seen.append(node)
                
            minweight = -1
            minnode = ''
            for connection, weight in connections.iteritems():
                print node, connection, weight
                if weight < minweight or minweight == -1:
                    minweight = weight
                    minnode = connection
            if minweight > -1:
                if not mstree.hasNode(minnode):
                    mstree.addNode(minnode)
                if not mstree.hasNode(node):
                    mstree.addNode(node)
                mstree.connect(node, minnode, minweight)
                if not components.has_key(node) and not components.has_key(minnode):
                    components[node] = node
                    components[minnode] = node
                elif components.has_key(node) and not components.has_key(minnode):
                    components[minnode] = components[node]
                elif components.has_key(minnode) and not components.has_key(node):
                    components[node] = components[minnode]
                else:
                    test = components[minnode]
                    rep = components[node]
                    for key in components.iterkeys():
                        if components[key] == test:
                            components[key] = rep

                print minweight, mstree.graphweight()
        print mstree.printGraph()
        print components
        print mstree.graphweight()



file = open('../data/data-prob107-easy.txt')
g = graph()

for i, line in enumerate(file.readlines()):
    if not g.hasNode(int(i)):
        g.addNode(int(i))
    for j, connection in enumerate(line.strip().split(',')):
        if connection != '-':
            if not g.hasNode(int(j)):
                g.addNode(int(j))

            g.connect(int(i), int(j), int(connection))

smallg = graph()

for a in g.nodes():
    for b in g.nodes():
        if a != b:
            path, cost = g.shortestPath(a, b)
            for i in range(len(path) - 1):
                cona = min(path[i], path[i + 1])
                conb = max(path[i], path[i + 1])
                if not smallg.hasNode(cona):
                    smallg.addNode(cona)
                if not smallg.hasNode(conb):
                    smallg.addNode(conb)
                smallg.connect(cona, conb, g.getweight(cona, conb))

print smallg.mst()
print smallg.graphweight()
#print smallg.printGraph()
#print g.graphweight()
#print g.shortestPath(0, 6)
