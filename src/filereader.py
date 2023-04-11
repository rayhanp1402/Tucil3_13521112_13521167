from node import Node

def readFile(filename):
    text = ""
    with open(filename) as file:
        for line in file:
            text += line.rstrip()
            text += '\n'

    return text


def ignoreFirstLine(filename):
    # Ignores the first line of text in the text file "filename"
    # Returns the index of the second line of text
    text = readFile(filename)
    i = 0
    while(text[i] != '\n'):
        i += 1

    return i + 1


def getNoOfNodes(filename):
    text = readFile(filename)
    noOfNodes = ""
    i = 0
    while(text[i] != '\n'):
        noOfNodes += text[i]
        i += 1

    return int(noOfNodes)


def generateNodes(filename):
    x = ""
    y = ""
    nodeName = ""
    nodes = []
    text = readFile(filename)

    i = ignoreFirstLine(filename)  
    for j in range(getNoOfNodes(filename)):
        while(text[i] == ' '):
            i += 1

        while(text[i] != ' '):
            nodeName += text[i]
            i += 1

        while(text[i] == ' '):
            i += 1

        while(text[i] != ' '):
            x += text[i]
            i += 1

        while(text[i] == ' '):
            i += 1

        while(text[i] != '\n'):
            y += text[i]
            i += 1

        nodes.append(Node(nodeName, float(x), float(y), j))
        nodeName = ""
        x = ""
        y = ""
        i += 1

    return nodes

        
def generateAdjacencyMatrix(filename):
    adjacencyMatrix = [[]]
    currentRow = 0
    text = readFile(filename)
    firstIdx = ignoreFirstLine(filename)
    elmt = ""
    i = firstIdx
    while(i < len(text) - 1):
        if(text[i] != ' ' and text[i] != '\n'):
            while(text[i] != ' ' and text[i] != '\n'):
                elmt += text[i]
                i += 1
            adjacencyMatrix[currentRow].append(float(elmt))
            elmt = ""

        if(text[i] == '\n'):
            adjacencyMatrix.append([])
            currentRow += 1

        i += 1

    adjacencyMatrix.pop()

    return adjacencyMatrix



# Filereader Test
# nodes = generateNodes("test/test.txt")
# adjacencyMatrix = generateAdjacencyMatrix("test/test.txt")

# for i in range(len(nodes)):
#     print("Node " + nodes[i].name + " : x=" + str(nodes[i].x) + " : y=" + str(nodes[i].y) + " : idx=" + str(nodes[i].idx))

# print(adjacencyMatrix)