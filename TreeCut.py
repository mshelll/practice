#!/bin/python3

import math
import os
import random
import re
import sys

from guppy import hpy

#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict

sys.setrecursionlimit(10000)

#
# Complete the 'cutTheTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY data
#  2. 2D_INTEGER_ARRAY edges
#

class Graph:
    def __init__(self):
        self.adj = defaultdict(list)

    def add_node(self, node, value):
        self.data[node] = value
    
    def add_edge(self, edge):
        x, y = edge
        self.adj[x].append(y)
        self.adj[y].append(x)


N = 0
g = None
ans = sys.maxsize

def dfsUtil(node, visited, value, total, parent):
    visited[node] = 1

    for cur in g.adj[node]:
        if visited[cur] == 0:
            dfsUtil(cur, visited, value, total, node)
            value[node] += value[cur]

    print("node :", node)
    print("parent :", parent)
    print("node value :", value[node])
    global ans
    if (node != 1):
      ans = min (ans, abs (total - 2 * value[node]))

    #print("ans :", ans)

    return ans
    



def dfs2(start, value, total):
    visited = [0]*(len(value)+1)
    return dfsUtil(start, visited, value, total, None)
    

def cutTheTree(data, edges):
    # Write your code here
    # global N
    # N = len(data)

    global g
    g = Graph()

    for edge in edges:
        g.add_edge(edge)

    print("Adj : ", g.adj)

    total_sum = sum(data)

    print("total :", total_sum)

    dfs2(1, [0]+data, total_sum)



    global ans
    print("ans :", ans)
    return ans

if __name__ == '__main__':
    fptr = open("/Users/rift/Workspace/python/input.txt", 'r')

    # print(fptr.read())

    n = int(fptr.readline().strip())

    print("n :", n)

    
    h = hpy()
    data = list(map(int, fptr.readline().rstrip().split()))

    edges = []

    for _ in range(n - 1):
        edges.append(list(map(int, fptr.readline().rstrip().split())))

    result = cutTheTree(data, edges)

    #fptr.write(str(result) + '\n')

    print("heap :", h.heap())

    fptr.close()
