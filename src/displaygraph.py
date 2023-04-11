import networkx as nx
import matplotlib.pyplot as plt
# import filereader
# import ucs

def checkIfPath(node1, node2, path):
    if(len(path) == 2):
        if(path[0] == node1.name):
            return True
        if(path[1] == node1.name):
            return True
    else:
        for i in range(1, len(path)-1):
            if(path[i] == node1.name):
                if(path[i-1] == node2.name or path[i+1] == node2.name):
                    return True
            
            if(path[i] == node2.name):
                if(path[i-1] == node1.name or path[i+1] == node1.name):
                    return True
        
    return False

def displayGraph(nodes, adjacencyMatrix, path):
    G = nx.Graph()
    edgeColor = 'b'

    for i in range(len(nodes)):
        G.add_node(nodes[i].name, pos=(nodes[i].x, nodes[i].y))
        for j in range(len(nodes)):
            if(adjacencyMatrix[i][j] > 0):
                if(checkIfPath(nodes[i], nodes[j], path)):
                    edgeColor = 'r'
                G.add_edge(nodes[i].name, nodes[j].name, color=edgeColor, weight=adjacencyMatrix[i][j])
                edgeColor = 'b'

    pos = nx.get_node_attributes(G,'pos')

    options = {
        "font_size": 24,
        "node_size": 1000,
        "node_color": "skyblue",
        "linewidths": 5,
        "width": 5,
    }
    edges = G.edges()
    colors = [G[u][v]['color'] for u,v in edges]
    weights = [G[u][v]['weight'] for u,v in edges]

    nx.draw_networkx(G, pos, edges, edge_color=colors, **options)

    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)

    # Set margins for the axes so that nodes aren't clipped
    ax = plt.gca()
    ax.margins(0.10)
    plt.axis("off")
    plt.show()



# Display Graph Test
# nodes = filereader.generateNodes("test/test.txt")
# adjacencyMatrix = filereader.generateAdjacencyMatrix("test/test.txt")
# startNode = nodes[0]
# goalNode = nodes[-1]

# result = ucs.uniformCostSearch(nodes, adjacencyMatrix, startNode, goalNode)
# path = ucs.constructPath(result)

# displayGraph(nodes, adjacencyMatrix, path)