from queue import PriorityQueue
from livenode import LiveNode
from node import Node
# import filereader

def uniformCostSearch(nodes, adjacencyMatrix, startNode, goalNode):
    prioQueue = PriorityQueue()
    currentNode = LiveNode(Node(startNode.name, startNode.x, startNode.y, startNode.idx))

    while(currentNode.node.name != goalNode.name):
        # Iterate through all the currentNode neighbors and push them into the prioqueue
        # The prioqueue will check based on Cost of traversal so far
        for i in range(len(adjacencyMatrix[currentNode.node.idx])):
            if(adjacencyMatrix[currentNode.node.idx][i] > 0):
                liveNode = LiveNode(Node(nodes[i].name, nodes[i].x, nodes[i].y, nodes[i].idx))
                liveNode.addCost(adjacencyMatrix[currentNode.node.idx][i])
                liveNode.addPrevNode(currentNode)

                liveNode.defineCompValue(liveNode.costSoFar)    # Using f(n), evaluation with minimum traversal Cost so far

                prioQueue.put(liveNode)

        currentNode = prioQueue.get()

    return currentNode


def reverseString(string):
    reversedString = ""
    for i in range(len(string)-1, -1, -1):
        reversedString += string[i]

    return reversedString


def constructPath(liveNode):
    path = []
    prevNodeName = ""
    i = len(liveNode.prevNodes) - 1
    while (i > -1):
        while(liveNode.prevNodes[i] != ' '):
            prevNodeName += liveNode.prevNodes[i]
            i -= 1

        prevNodeName = reverseString(prevNodeName)
        path.append(prevNodeName)
        prevNodeName = ""
        i -= 1

    if(len(path) > 0):
        del path[0]
    path.append(liveNode.node.name)

    return path


def printPath(path):
    for i in range(len(path)):
        if(i != len(path) - 1):
            print(path[i] + " -> ", end="")
        else:
            print(path[i])