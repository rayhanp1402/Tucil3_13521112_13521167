import filereader
import ucs
import displaygraph
import os.path


fileFound = False

while(not(fileFound)):
    filename = input("Masukkan nama file (bukan path) : ")
    filename = "test/" + filename

    if os.path.exists(filename):
        fileFound = True
        nodes = filereader.generateNodes(filename)
        adjacencyMatrix = filereader.generateAdjacencyMatrix(filename)
        startNode = nodes[0]
        goalNode = nodes[-1]

        result = ucs.uniformCostSearch(nodes, adjacencyMatrix, startNode, goalNode)

        path = ucs.constructPath(result)
        ucs.printPath(path)

        print("Cost = " + str(result.costSoFar))

        displaygraph.displayGraph(nodes, adjacencyMatrix, path)
        
    else:
        print("File tidak ditemukan. Coba lagi\n")
        