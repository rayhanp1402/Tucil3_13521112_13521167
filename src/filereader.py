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


def generateNodes(filename):
    x = ""
    y = ""
    nodeName = ""
    idx = 0
    i = 0
    nodes = []
    isCoordinate = False
    text = readFile(filename)
    
    while(text[i] != '\n'):
        if(text[i] == '('):
            isCoordinate = True

        if(text[i] != ' ' and not(isCoordinate) and text[i] != ')'):
            nodeName = text[i]

        if(text[i] != ' ' and isCoordinate and text[i] != '('):
            while(text[i] != ','):
                x += text[i]
                i += 1
            i += 1
            while(text[i] != ')'):
                y += text[i]
                i += 1

            nodes.append(Node(nodeName, float(x), float(y), idx))
            x = ""
            y = ""
            idx += 1
            isCoordinate = False

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