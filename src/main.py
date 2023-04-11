import filereader
import ucs
import displaygraph
import os.path

def getNode(nodes, targetNodeName):
    for i in range(len(nodes)):
        if(nodes[i].name == targetNodeName):
            return nodes[i]
    return None

def inputNode(nodes):
    nodeFound = False
    startNode = nodes[0]
    endNode = nodes[-1]
    while(not(nodeFound)):
        startNodeInput = input("Masukkan start node : ")
        if(getNode(nodes, startNodeInput) == None):
            print("Node tidak ditemukan. Coba lagi\n")
        else:
            startNode = getNode(nodes, startNodeInput)
            nodeFound = True
    
    nodeFound = False
    while(not(nodeFound)):
        endNodeInput = input("Masukkan end node : ")
        if(getNode(nodes, endNodeInput) == None):
            print("Node tidak ditemukan. Coba lagi\n")
        else:
            endNode = getNode(nodes, endNodeInput)
            nodeFound = True

    return (startNode, endNode)




def main():
    fileFound = False

    while(not(fileFound)):
        filename = input("Masukkan nama file txt (bukan path & tanpa .txt) : ")
        filename = "test/" + filename + ".txt"

        if os.path.exists(filename):
            fileFound = True
            nodes = filereader.generateNodes(filename)
            adjacencyMatrix = filereader.generateAdjacencyMatrix(filename)
            startEndNode = inputNode(nodes)
            startNode = startEndNode[0]
            goalNode = startEndNode[1]

            result = ucs.uniformCostSearch(nodes, adjacencyMatrix, startNode, goalNode)

            path = ucs.constructPath(result)
            ucs.printPath(path)

            print("Cost = " + str(result.costSoFar))

            displaygraph.displayGraph(nodes, adjacencyMatrix, path)
            
        else:
            print("File tidak ditemukan. Coba lagi\n")


main()