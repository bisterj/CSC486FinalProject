import networkx as nx
import matplotlib.pyplot as plt
import Caterpillar_Graph

prufer = []

G = Caterpillar_Graph.caterpillar_graph(2, 3)

nx.draw_networkx(G)
plt.show()

nodes = list(G.nodes())
print(len(nodes))

leaves = []

for node in nodes:
    if G.degree[node] == 1:
        leaves.append(node)

for i in range(len(nodes) - 2):
    target = min(leaves)

    for edge in list(G.edges()):
        if target in edge:
            if edge.index(target) == 1:
                prufer.append(edge[0])
                leaves.remove(target)
                G.remove_node(target)
                if G.degree[edge[0]] == 1:
                    leaves.append(edge[0])
            else:
                prufer.append(edge[1])
                leaves.remove(target)
                G.remove_node(target)
                if G.degree[edge[1]] == 1:
                    leaves.append(edge[1])

print(prufer)
