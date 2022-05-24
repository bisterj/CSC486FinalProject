import matplotlib.pyplot as plt
import networkx as nx
import copy

prufer = [1, 7, 3, 7, 5, 5, 15, 9, 9, 15, 10, 10, 8, 7, 15, 16, 17, 17, 17]
temp = copy.deepcopy(prufer)

G = nx.Graph()
complete = []

for i in range(len(prufer) + 2):
    G.add_node(i)
    complete.append(i)

for digit in prufer:
    diff = list(set(complete) - set(temp))
    num = min(diff)
    G.add_edge(digit, num)
    temp.remove(digit)
    temp.append(num)

diff = list(set(complete) - set(temp))
G.add_edge(diff[0], diff[1])

nx.draw_networkx(G)
plt.show()