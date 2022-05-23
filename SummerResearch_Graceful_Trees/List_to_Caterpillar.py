import networkx as nx
import matplotlib.pyplot as plt

caterpillar = [1, 2, 1, 3]

G = nx.path_graph(len(caterpillar))

size = len(list(G.nodes()))
for i in range(len(caterpillar)):
    size = len(list(G.nodes()))
    for r in range(caterpillar[i]):
        G.add_node(size + r)
        G.add_edge(i, size + r)

nx.draw_networkx(G)
plt.show()