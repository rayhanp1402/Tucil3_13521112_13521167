import os
import numpy as np
import pandas as pd
from collections import defaultdict

def haversine(kota1,kota2):
    r = 6371
    body = np.sin((kota1[0]-kota2[0])/2)**2 + np.cos(kota1[0])*np.cos(kota2[0])*(np.sin((kota2[1]-kota1[1])/2))**2 
    return 2*r*np.arcsin(np.sqrt(body))

def heuristics(akar_node, tujuan_node):
    for i in range(len(akar_node[1])):
        if akar_node[1][i] == tujuan_node:
            end = i
    dgoal = []

    a={}

    for i in range(len(akar_node[1])):
        dgoal.append(haversine(akar_node[2][end],akar_node[2][i]))
        a[akar_node[1][i]] = dgoal[i]
    return a
def sorting (list, dic):
    value_dic = {}
    for node in list:
        if dic.get(node, "Not Available") != "Not Available":
          value_dic[node] = dic[node]
    value_dic = dict(sorted(value_dic.items(), key=lambda item: item[1]))
    sorted = []
    for i in value_dic.keys():
      sorted.append(i)
    return sorted

def find_low_cost(list_to_sort):
    """
    This function returns the name of the city that have the lower cost in list_to_sort
      :para list_to_sort (list): the list of tuples that contains the city point information
      :return: the name of the city with lower estimated total cost f
    """
    return sorted(list_to_sort, key=lambda x: x[1])[0][0]


def astar_search(akar_node, heuristics, start_node, goal_node): 
    
    #ketika node kosong, lalu mau di isi
    buka_node = []
    tutup_node = []

    # Bikin dictionary prev, key = node dan value = parent node
    prev = {}
    for i in akar_node[1]:
      prev[i] = None

    # Bikin dictionary B value, D value
    dictB= {}
    dictB[start_node] = heuristics[start_node]

    dictD = {}
    dictD[start_node] = 0


    buka_node.append(start_node)
    
    # looping open
    while len(buka_node) > 0:
        # mencari value terkecil
        buka_node = find_low_cost(buka_node, dictB)
        node_now = buka_node.pop(0)
        tutup_node.append(node_now)

        # Jika sudah mencapai simpul tujuan
        if node_now == goal_node:
            path = []
            while node_now != start_node:
                path.append(node_now)
                node_now = prev[node_now]
            path.append(start_node)
            return path[::-1]

        # looping simpul tetangga dari current node
        node_tetangga = akar_node[0][node_now]  

        for neighbor in node_tetangga.keys():    
            # Kasus simpul sudah diperiksa
            if(neighbor in tutup_node):
                continue
            prev[neighbor] = node_now

            # Update nilai D value dan B value jika B value baru lebih minimum
            if(dictD[node_now] + node_tetangga[neighbor] + heuristics[neighbor] < dictB.get(neighbor, 99999999)):
              dictD[neighbor] = dictD[node_now] + node_tetangga[neighbor] 
              dictB[neighbor] = dictD[neighbor] + heuristics[neighbor]
              buka_node.append(neighbor)
    # Return None jika tidak ada jalur
    return None