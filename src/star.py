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
