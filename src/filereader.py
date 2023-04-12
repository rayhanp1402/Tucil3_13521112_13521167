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


def ignoreNodes(filename):
    # Ignores the node lines in the file text "filename"
    # Returns the first index of the adjacency matrix line in the file text
    text = readFile(filename)
    i = ignoreFirstLine(filename)
    for j in range(getNoOfNodes(filename)):
        while(text[i] != '\n'):
            i += 1
        i += 1
    return i

        
def generateAdjacencyMatrix(filename):
    adjacencyMatrix = []
    text = readFile(filename)
    elmt = ""

    i = ignoreNodes(filename)
    for j in range(getNoOfNodes(filename)):
        adjacencyMatrix.append([])
        while(text[i] != '\n'):
            while(text[i] == ' '):
                i += 1

            while(text[i] != ' ' and text[i] != '\n'):
                elmt += text[i]
                i += 1

            adjacencyMatrix[j].append(float(elmt))
            elmt = ""

            while(text[i] == ' '):
                i += 1

        i += 1
    
    return adjacencyMatrix