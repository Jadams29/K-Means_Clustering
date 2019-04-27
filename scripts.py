import math




class Centroid:
    def __init__(self, nodes=[], centroid_node=None, x=0, y=0, centroid_color='black', node_color='black'):
        self.nodes = nodes
        self.centroid_node = centroid_node
        self.centroid_color = centroid_color
        self.node_color = node_color
        self.x = x
        self.y = y


class Node:
    def __init__(self, x=0, y=0):
        self.x = float(x)
        self.y = float(y)


def distance(node1, node2):
    # sqrt( (X1-X2)^2 + (Y1-Y2)^2 )
    return math.sqrt(math.pow((node1.x - node2.x), 2) + math.pow((node1.y - node2.y), 2))


def distance1(x1, y1, x2, y2):
    # sqrt( (X1-X2)^2 + (Y1-Y2)^2 )
    return math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2))
