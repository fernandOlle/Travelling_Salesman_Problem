from sys import maxsize
from itertools import permutations
from numpy import loadtxt
import time

def travellingSalesmanProblem(graph, s):
    start_time =  time.time()
    V = len(graph)
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)
    min_path = maxsize
    next_permutation=permutations(vertex)
    for i in next_permutation:
        current_pathweight = 0
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]
        min_path = min(min_path, current_pathweight)
    print("tempo: %s"%(time.time() - start_time))        
    return min_path
 
if __name__ == "__main__":
    # graphMatrix = loadtxt('tsp_data/tsp1_253.txt', dtype=int)
    # graphMatrix = loadtxt('tsp_data/tsp2_1248.txt', dtype=int)
    graphMatrix = loadtxt('tsp_data/tsp3_1194.txt', dtype=int)
    # graphMatrix = loadtxt('tsp_data/tsp4_7013.txt', dtype=int)
    # graphMatrix = loadtxt('tsp_data/tsp5_27603.txt', dtype=int)
    s = 0
    print(travellingSalesmanProblem(graphMatrix, s))