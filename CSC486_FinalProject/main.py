from random import choice

import networkx as nx
import matplotlib.pyplot as plt

# A few structures that make translating from actions to indices to scores easier
action_list = ["talk", "listen", "ignore"]
action_lookup = {"talk": 0, "listen": 1, "ignore": 2}
payoff_matrix = [[(-1, -1), (10, 5), (-5, 0)],
                 [(5, 10), (-1, -1), (0, 5)],
                 [(0, -5), (5, 0), (0, 0)]]


def random_update(G):
    """
    This update function chooses a random node and gives the node
    a random action from the list of available actions
    :param G:
    :return: None
    """
    nodes = list(G.nodes())
    # chooses a random node to change the action randomly
    node_to_update = choice(nodes)
    nbrs = G.neighbors(node_to_update)

    # stores the old action
    old_action = G.nodes[node_to_update]["action"]

    # chooses a new action for the randomly chosen node
    new_action = choice(["talk", "listen", "ignore"])
    G.nodes[node_to_update]["action"] = new_action

    # gets all the actions that the neighbors of the central node
    nbr_actions = []
    for nbr in nbrs:
        nbr_actions.append(G.nodes[nbr]["action"])

    # updates the neighbors of the node by taking away the old score given by the central node and add the
    # new score added by the central node
    for nbr in nbrs:
        print(old_action)
        old_score = payoff_matrix[action_lookup[old_action]][action_lookup[nbr_actions[nbr]]]
        G.nodes[nbr]["score"] -= old_score[1]

        new_score = payoff_matrix[action_lookup[new_action]][action_lookup[nbr_actions[nbr]]]
        G.nodes[nbr]["score"] += new_score[1]

    # updates the score for the central node by adding the scores given by the neighbors
    G.nodes[node_to_update]["score"] = 0
    for action in nbr_actions:
        score = payoff_matrix[action_lookup[new_action]][action_lookup[action]]
        G.nodes[node_to_update]["score"] += score[0]


def greedy_update(G):
    """
    This update function chooses a random node to change their action but
    the action is chosen by maximizing the score for the chosen node
    :param G:
    :return: None
    """
    nodes = list(G.nodes())
    # chooses a random node to change the action randomly
    node_to_update = choice(nodes)
    nbrs = G.neighbors(node_to_update)

    # stores the old action
    old_action = G.nodes[node_to_update]["action"]

    # gets all the actions that the neighbors of the central node
    nbr_actions = []
    for nbr in nbrs:
        nbr_actions.append(G.nodes[nbr]["action"])

    # finds the new action by looking at which action will give the current node the highest total score
    new_action = old_action
    max_score = -99
    for action in action_list:
        curr_score = 0
        for nbr_action in nbr_actions:
            score = payoff_matrix[action_lookup[action]][action_lookup[nbr_action]]
            curr_score += score[0]
        if curr_score > max_score:
            max_score = curr_score
            new_action = action

    # updates the neighbors of the node by taking away the old score given by the central node and add the
    # new score added by the central node
    for nbr in nbrs:
        print(old_action)
        old_score = payoff_matrix[action_lookup[old_action]][action_lookup[nbr_actions[nbr]]]
        G.nodes[nbr]["score"] -= old_score[1]

        new_score = payoff_matrix[action_lookup[new_action]][action_lookup[nbr_actions[nbr]]]
        G.nodes[nbr]["score"] += new_score[1]

    # updates the score for the central node by adding the scores given by the neighbors
    G.nodes[node_to_update]["score"] = 0
    for action in nbr_actions:
        score = payoff_matrix[action_lookup[new_action]][action_lookup[action]]
        G.nodes[node_to_update]["score"] += score[0]


def maximize_update(G):
    """
    This update function chooses a node randomly and then changes
    the action of that node that will maximize the score of itself
    and its neighbors
    :param G:
    :return: None
    """
    nodes = list(G.nodes())
    # chooses a random node to change the action randomly
    node_to_update = choice(nodes)
    nbrs = G.neighbors(node_to_update)

    # stores the old action
    old_action = G.nodes[node_to_update]["action"]

    # gets all the actions that the neighbors of the central node
    nbr_actions = []
    for nbr in nbrs:
        nbr_actions.append(G.nodes[nbr]["action"])

    # finds the new action by looking at which action will give the whole community
    # the highest total score

    new_action = old_action
    max_score = -99
    for action in action_list:
        curr_score = 0
        for nbr_action in nbr_actions:
            score = payoff_matrix[action_lookup[action]][action_lookup[nbr_action]]
            curr_score += score[0]
            curr_score += score[1]
        if curr_score > max_score:
            max_score = curr_score
            new_action = action

    # updates the neighbors of the node by taking away the old score given by the central node and add the
    # new score added by the central node
    for nbr in nbrs:
        print(old_action)
        old_score = payoff_matrix[action_lookup[old_action]][action_lookup[nbr_actions[nbr]]]
        G.nodes[nbr]["score"] -= old_score[1]

        new_score = payoff_matrix[action_lookup[new_action]][action_lookup[nbr_actions[nbr]]]
        G.nodes[nbr]["score"] += new_score[1]

    # updates the score for the central node by adding the scores given by the neighbors
    G.nodes[node_to_update]["score"] = 0
    for action in nbr_actions:
        score = payoff_matrix[action_lookup[new_action]][action_lookup[action]]
        G.nodes[node_to_update]["score"] += score[0]


def print_scores(G):
    """
    This function is a helper to see what the graph
    looks like and what the total score is
    :param G:
    :return: None
    """
    nodes = list(G.nodes())
    for node in nodes:
        nbrs = []
        for i in G.neighbors(node):
            nbrs.append(i)
        print(node)
        print(G.nodes[node])
        print(nbrs)
    sum = 0
    for node in nodes:
        sum += G.nodes[node]["score"]
    print("TOTAL SCORE: ", sum)
    print("AVG: SCORE: ", sum / len(nodes))


def connect_edge_edges(G):
    """
    Helper function that connects nodes that only have to edges connected to
    ensure that every node has a degree of three, This fixes the hexagonal_lattice_graph()
    from networkx so that it can be used for this graph
    :param G:
    :return: None
    """

    nodes = list(G.nodes())
    degree_node_pairs = G.degree()
    degrees_to_connect = []

    for pair in degree_node_pairs:
        if pair[1] < 3:
            degrees_to_connect.append(pair)

    for i in range(len(degrees_to_connect) // 2):
        size = len(degrees_to_connect)
        G.add_edge(degrees_to_connect[i][0], degrees_to_connect[size - i - 1][0])


def get_score(G, node):
    return G.nodes[node]["score"]


def get_avg_score(G):
    nodes = list(G.nodes)
    sum = 0
    for node in nodes:
        sum += G.nodes[node]["score"]
    return sum / len(nodes)


def plot_line(y_values):
    x_axis = []
    for i in range(len(y_values)):
        x_axis.append(i + 1)
    plt.plot(x_axis, y_values)
    plt.title('Total Score of Network Over Time')
    plt.xlabel('Steps')
    plt.ylabel('Total Score')
    plt.show()


def main():
    # Creates the graph structure closest to what we need (All nodes with 3 edges)
    G = nx.hexagonal_lattice_graph(20, 20)

    # Creates edges between nodes that only have two edges to achieve the desired graph structure
    connect_edge_edges(G)

    # Create a list that is the list of nodes
    nodes = list(G.nodes())

    # initializes the attributes score and action
    for node in nodes:
        G.nodes[node]["score"] = 0
        G.nodes[node]["action"] = choice(["talk", "listen", "ignore"])

    # updates the score based on the payoff matrix
    for node in nodes:
        nbrs = G.neighbors(node)
        nbr_actions = []
        node_action = G.nodes[node]["action"]
        for nbr in nbrs:
            nbr_actions.append(G.nodes[nbr]["action"])
        for action in nbr_actions:
            score = payoff_matrix[action_lookup[node_action]][action_lookup[action]]
            G.nodes[node]["score"] += score[0]

    # A list to collect the data we want to plot
    data = []

    # # iterates the update 100 times
    # for i in range(100):
    #     # calculates the total score of the network
    #     sum = 0
    #     for node in nodes:
    #         sum += get_score(G, node)
    #     data.append(sum)
    #     random_update(G)

    # gathers average score at each update function call
    for i in range(100):
        avg = get_avg_score(G)
        data.append(avg)
        greedy_update(G)
    # PLots a line graph
    plot_line(data)

    # # Calls the function to see what the graph looks like and what the total score is and average score
    # print_scores(G)
    # pos = nx.spring_layout(G)
    # nx.draw_networkx(G, pos)
    # plt.show()


main()


