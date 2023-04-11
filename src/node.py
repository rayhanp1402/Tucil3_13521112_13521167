import math

class Node:
    def __init__(self, name, x, y, idx):
        self.name = name
        self.x = x
        self.y = y
        self.idx = idx  # Index of the node in the adjacency matrix
        self.distance = 0   # The Euclidean Distance of this Node to another Node

    def euclideanDistance(self, otherNode):
        self.distance = math.sqrt(math.pow((self.x - otherNode.x), 2) + math.pow((self.y - otherNode.y), 2))