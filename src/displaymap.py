import folium
import pandas as pd
import networkx as nx
import main
from displaygraph import checkIfPath

def fillArrayFromNodeField(nodes, attribute):
    # Returns an array with the nodes attributes
    attributes = []
    for i in range(len(nodes)):
        if(attribute == 'name'):
            attributes.append(nodes[i].name)
        if(attribute == 'x'):
            attributes.append(nodes[i].x)
        if(attribute == 'y'):
            attributes.append(nodes[i].y)

    return attributes



def createMap(nodes, adjacencyMatrix, path):
    lon = fillArrayFromNodeField(nodes, 'y')
    lat = fillArrayFromNodeField(nodes, 'x')
    name = fillArrayFromNodeField(nodes, 'name')
    # Make a data frame with dots to show on the map
    data = pd.DataFrame({
    'lon':lon,
    'lat':lat,
    'name':name,
    }, dtype=str)

    m = folium.Map()
    # add marker one by one on the map
    for i in range(0,len(data)):
        folium.Marker(
            location=[data.iloc[i]['lat'], data.iloc[i]['lon']],
            popup=data.iloc[i]['name'],
        ).add_to(m)

    # Add routes
    edgeColor = 'blue'
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            if(adjacencyMatrix[i][j] > 0):
                if(checkIfPath(nodes[i], nodes[j], path)):
                    edgeColor = 'red'

                loc = [(nodes[i].x, nodes[i].y),
                       (nodes[j].x, nodes[j].y)]

                folium.PolyLine(loc,
                            color=edgeColor,
                            opacity=0.8).add_to(m)
                edgeColor = 'blue'

    m.save("map.html")


# Display Map Test
# nodes = main.filereader.generateNodes("test/europecapitals.txt")
# adjacencyMatrix = main.filereader.generateAdjacencyMatrix("test/europecapitals.txt")
# result = main.ucs.uniformCostSearch(nodes, adjacencyMatrix, nodes[2], nodes[4])
# path = main.ucs.constructPath(result)
# createMap(nodes, adjacencyMatrix, path)