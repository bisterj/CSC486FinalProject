import networkx as nx
import matplotlib.pyplot as plt
import random as r


def caterpillar_graph(n, k):
    """
    creates a caterpillar graph, a graph with a central path and leaf nodes coming off the nodes of said central path
    :param n: number of nodes on central path
    :param k: max number of leaf nodes per central path node, actual number of leaf nodes is random
    :return: Graph G which is a caterpillar graph
    """

    G = nx.path_graph(n)

    nodes = list(G.nodes())

    for node in nodes:
        for i in range(r.randint(0, k)):
            G.add_node(len(G.nodes()))
            new_node = max(list(G.nodes))
            G.add_edge(node, new_node)
    return G


# creates a caterpillar graph with 5 central nodes and up to 2 leaves per central node
G = caterpillar_graph(5, 2)
nodes = list(G.nodes())

edges = list(G.edges())

# calculates induced labellings
for edge in edges:
    node1 = edge[0]
    node2 = edge[1]
    G[node1][node2]['label'] = abs(node1 - node2)

# draws graph so that a window will popup with the graph
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos)
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()