from queue import PriorityQueue
from livenode import LiveNode
from node import Node
import filereader

def uniformCostSearch(nodes, adjacencyMatrix, startNode, goalNode):
    prioQueue = PriorityQueue()
    currentNode = LiveNode(Node(startNode.name, startNode.x, startNode.y, startNode.idx))

    while(currentNode.node.name != goalNode.name):
        # Iterate through all the currentNode neighbors and push them into the prioqueue
        for i in range(len(adjacencyMatrix[currentNode.node.idx])):
            if(adjacencyMatrix[currentNode.node.idx][i] > 0):
                liveNode = LiveNode(Node(nodes[i].name, nodes[i].x, nodes[i].y, nodes[i].idx))
                liveNode.addCost(adjacencyMatrix[currentNode.node.idx][i])
                liveNode.addPrevNode(currentNode)
                prioQueue.put(liveNode)

        currentNode = prioQueue.get()

    return currentNode


def constructPath(liveNode):
    path = []
    for i in range(len(liveNode.prevNodes)-1, -1, -1):
        path.append(liveNode.prevNodes[i])

    path.append(liveNode.node.name)

    return path


def printPath(path):
    for i in range(len(path)):
        if(i != len(path) - 1):
            print(path[i] + " -> ", end="")
        else:
            print(path[i])


# UCS Test
nodes = filereader.generateNodes("test/test.txt")
adjacencyMatrix = filereader.generateAdjacencyMatrix("test/test.txt")
startNode = nodes[0]
goalNode = nodes[-1]

result = uniformCostSearch(nodes, adjacencyMatrix, startNode, goalNode)
print("Node = " + result.node.name)

path = constructPath(result)
printPath(path)

print("Cost = " + str(result.costSoFar))