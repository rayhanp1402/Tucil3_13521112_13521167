import math
import numpy as np

class Node:
    def __init__(self, name, x, y, idx):
        self.name = name
        self.x = x
        self.y = y
        self.idx = idx  # Index of the node in the adjacency matrix
        self.distance = 0   # The Euclidean Distance of this Node to another Node

    def euclideanDistance(self, otherNode):
        self.distance = math.sqrt(math.pow((self.x - otherNode.x), 2) + math.pow((self.y - otherNode.y), 2))

    def haversineDistance(self, otherNode):
        r = 6371
        body = np.sin((self.x - otherNode.x)/2)**2 + np.cos(self.x)*np.cos(otherNode.x)*(np.sin((otherNode.y - self.y)/2))**2 
        self.distance = 2*r*np.arcsin(np.sqrt(body))