class LiveNode:
    def __init__(self, node): # node is an instance of the class Node
        self.node = node
        self.prevNodes = ""
        self.costSoFar = 0
        self.compValue = 0  # Value used for comparison in a priority queue

    def __lt__(self, otherLiveNode):
        return self.compValue < otherLiveNode.compValue

    def addPrevNode(self, prevNode): # prevNode an instance of the class LiveNode
        self.prevNodes += prevNode.node.name + ' ' + prevNode.prevNodes
        self.costSoFar += prevNode.costSoFar

    def addCost(self, cost):
        self.costSoFar += cost

    def defineCompValue(self, compValue):
        self.compValue = compValue