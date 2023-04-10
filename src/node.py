import math

class Node:
    def __init__(self, name, x, y, idx):
        self.name = name
        self.x = x
        self.y = y
        self.idx = idx  # Index of the node in the adjacency matrix

    def euclideanDistance(self, otherNode):
        return math.sqrt(math.pow((self.x - otherNode.x), 2) + math.pow((self.y - otherNode.y), 2))