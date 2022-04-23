from random import choice

import networkx as nx
import matplotlib.pyplot as plt


action_lookup = {"talk": 0, "listen": 1, "ignore": 2}
payoff_matrix = [[(-1, -1), (10, 5), (-5, 0)],
                 [(5, 10), (-1, -1), (0, 5)],
                 [(0, -5), (5, 0), (0, 0)]]

def update_random():
    # chooses a random node to change the action randomly
    node_to_update = choice(nodes)
    nbrs = G.neighbors(node_to_update)

    # stores the old action
    old_action = G.nodes[node_to_update]["action"]

    # chooses a new action for the randomly chosen node
    new_action = choice(["talk", "listen", "ignore"])
    G.nodes[node_to_update]["action"] = new_action

    # updates the neighbors of the node by taking away the old score given by the central node and add the
    # new score added by the central node
    for nbr in nbrs:
        print(old_action)
        old_score = payoff_matrix[action_lookup[old_action]][action_lookup["talk"]]
        G.nodes[nbr]["score"] -= old_score[1]

        new_score = payoff_matrix[action_lookup["talk"]][action_lookup["talk"]]
        G.nodes[nbr]["score"] += new_score[1]

    # gets all the actions that the neighbors of the central node
    nbr_actions = []
    for nbr in nbrs:
        nbr_actions.append(G.nodes[nbr]["action"])

    # updates the score for the central node by adding the scores given by the neighbors
    G.nodes[node_to_update]["score"] = 0
    for action in nbr_actions:
        score = payoff_matrix[action_lookup[new_action]][action_lookup[action]]
        G.nodes[node_to_update]["score"] += score[0]


def print_scores():
    for i in G.nodes():
        list = []
        for i in G.neighbors(i):
            list.append(i+1)
        print(i)
        print(G.nodes[i])
        print(list)


G = nx.watts_strogatz_graph(12, 2, 0)

nodes = list(G.nodes())

for node in nodes:
    G.nodes[node]["score"] = 0
    G.nodes[node]["action"] = choice(["talk", "listen", "ignore"])

print_scores()

for node in nodes:
    nbrs = G.neighbors(node)
    nbr_actions = []
    node_action = G.nodes[node]["action"]
    for nbr in nbrs:
        nbr_actions.append(G.nodes[nbr]["action"])
    for action in nbr_actions:
        score = payoff_matrix[action_lookup[node_action]][action_lookup[action]]
        G.nodes[node]["score"] += score[0]


for i in range(100):
    update_random()
print_scores()

pos = nx.spring_layout(G)
nx.draw_networkx(G, pos)
plt.show()


