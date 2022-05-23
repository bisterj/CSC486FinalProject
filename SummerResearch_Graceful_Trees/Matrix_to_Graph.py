from math import sqrt

import networkx as nx
import matplotlib.pyplot as plt

# the matrix you want to convert, don't make it larger than necessary because it will create unwanted nodes
matrix = [[0, 1, 0, 1, 1, 1],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0]]

# creates a graph to have nodes and edges added
G = nx.Graph()

# adds nodes to the graph based on the size of the matrix
for i in range(len(matrix)):
    G.add_node(i)

# adds edges according to the matrix
for i in range(len(matrix)-1):
    row = matrix[i]
    for r in range(len(matrix) - (i + 1)):
        if row[r+i+1] == 1:
            G.add_edge(i, r+i+1)


# creates the induced edge labels
edges = list(G.edges())

for edge in edges:
    node1 = edge[0]
    node2 = edge[1]
    G[node1][node2]['label'] = abs(node1 - node2)

# draws the graph so that a window will popup with the graph
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos)
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()