import os.path
import filereader
import ucs
import star
import displaygraph
import displaymap

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


def inputAlgorithm(nodes, adjacencyMatrix, startNode, goalNode):
    validAlgo = False
    while(not(validAlgo)):
        print("Algoritma : ")
        print("1. Uniform Cost Search")
        print("2. A*")
        algo = input("Pilih nomor algoritma : ")

        if(algo == '1'):
            result = ucs.uniformCostSearch(nodes, adjacencyMatrix, startNode, goalNode)
            validAlgo = True
        elif(algo == '2'):
            heuristicType = inputHeuristic()
            result = star.astar_search(nodes, adjacencyMatrix, startNode, goalNode, heuristicType)
            validAlgo = True
        else:
            print("Input invalid. Coba lagi\n")

    return result


def inputHeuristic():
    validHeuristic = False
    while(not(validHeuristic)):
        print("Tipe Heuristik : ")
        print("1. Euclidean Distance")
        print("2. Haversine Distance")
        heuristicType = input("Pilih nomor heuristic : ")

        if(heuristicType == '1' or heuristicType == '2'):
            return heuristicType
        else:
            print("Input invalid. Coba lagi\n")


def display(nodes, adjacencyMatrix, path, startNode):
    validDisplay = False
    while(not(validDisplay)):
        print("Pilih display dengan : ")
        print("1. Network Graph")
        print("2. Map")
        displayType = input("Pilih nomor display : ")

        if(displayType == '1'):
            displaygraph.displayGraph(nodes, adjacencyMatrix, path)
            validDisplay = True
        elif(displayType == '2'):
            print('\nMembuat map . . .')
            displaymap.createMap(nodes, adjacencyMatrix, path, startNode)
            print("Map telah dibuat dengan file map.html pada root")
            validDisplay = True
        else:
            print("Input invalid. Coba lagi\n")

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

            result = inputAlgorithm(nodes, adjacencyMatrix, startNode, goalNode)

            path = ucs.constructPath(result)
            ucs.printPath(path)

            print("Cost = " + str(result.costSoFar))

            display(nodes, adjacencyMatrix, path, startNode)
            
        else:
            print("File tidak ditemukan. Coba lagi\n")


main()