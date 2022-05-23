import networkx as nx
import matplotlib.pyplot as plt

lobster = [[0, 0, 0], [2, 2]]

centres = len(lobster)

total = centres
for claw in lobster:
    total += len(claw)

G = nx.path_graph(len(lobster))
size = len(list(G.nodes()))
count = 0
branch = 0

for i in range(len(lobster)):
    for r in range(size, len(lobster[i]) + size):
        G.add_node(size + branch)
        G.add_edge(i, size + branch)
        branch += 1
        for c in range(total + count, lobster[i][r - size] + total + count):
            G.add_node(c)
            G.add_edge(c, size + branch -1)
            count += 1

pos = nx.spring_layout(G, iterations=100)
nx.draw_networkx(G)
plt.show()

