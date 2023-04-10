import networkx as nx
import matplotlib.pyplot as plt
import filereader

def displayGraph(nodes, adjacencyMatrix):
    G = nx.Graph()

    for i in range(len(nodes)):
        G.add_node(nodes[i].name, pos=(nodes[i].x, nodes[i].y))
        for j in range(len(nodes)):
            if(adjacencyMatrix[i][j] > 0):
                G.add_edge(nodes[i].name, nodes[j].name, weight=adjacencyMatrix[i][j])

    pos = nx.get_node_attributes(G,'pos')

    options = {
        "font_size": 30,
        "node_size": 2000,
        "node_color": "skyblue",
        "edgecolors": "black",
        "linewidths": 5,
        "width": 5,
    }

    nx.draw_networkx(G, pos, **options)

    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)

    # Set margins for the axes so that nodes aren't clipped
    ax = plt.gca()
    ax.margins(0.20)
    plt.axis("off")
    plt.show()



# Display Graph Test
nodes = filereader.generateNodes("test/test.txt")
adjacencyMatrix = filereader.generateAdjacencyMatrix("test/test.txt")
displayGraph(nodes, adjacencyMatrix)