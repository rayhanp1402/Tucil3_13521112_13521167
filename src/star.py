from queue import PriorityQueue
from node import Node
from livenode import LiveNode


def heuristics(akar_node, tujuan_node, heuristic_type):
    if(heuristic_type == '1'):
        akar_node.node.euclideanDistance(tujuan_node)
    else:
        akar_node.node.haversineDistance(tujuan_node)


def astar_search(nodes, adjacencyMatrix, start_node, goal_node, heuristic_type): 
    prioQueue = PriorityQueue()
    currentNode = LiveNode(Node(start_node.name, start_node.x, start_node.y, start_node.idx))
    currentNode.node.euclideanDistance(goal_node)

    while(currentNode.node.name != goal_node.name):
        # Iterate through all the currentNode neighbors and push them into the prioqueue
        # The prioqueue will check based on Euclidean/Haversine Distance + Cost of traversal so far (heuristics)
        for i in range(len(adjacencyMatrix[currentNode.node.idx])):
            if(adjacencyMatrix[currentNode.node.idx][i] > 0):
                liveNode = LiveNode(Node(nodes[i].name, nodes[i].x, nodes[i].y, nodes[i].idx))

                heuristics(liveNode, goal_node, heuristic_type)

                liveNode.addCost(adjacencyMatrix[currentNode.node.idx][i])
                liveNode.addPrevNode(currentNode)

                # Using f(n) + h(n)
                # Evaluation with the traversal Cost so far + Euclidean/Haversine Distance of the live node with the goal node
                liveNode.defineCompValue(liveNode.costSoFar + liveNode.node.distance)

                prioQueue.put(liveNode)

        currentNode = prioQueue.get()

    return currentNode