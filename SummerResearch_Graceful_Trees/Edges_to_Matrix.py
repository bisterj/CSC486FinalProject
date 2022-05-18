matrix = []
edges = [(0, 1), (1, 2), (0, 2)]
size = 3

# creates an empty matrix of the correct size
for r in range(size):
    temp = []
    for c in range(size):
        temp.append(0)
    matrix.append(temp)

# adds ones in the corresponding entry based on each edge
for edge in edges:
    node1 = edge[0]
    node2 = edge[1]
    matrix[node1][node2] = 1


# a better visualization of the matrix in string form
def matrix_to_string(m):
    string = ''
    for i in range(len(m)):
        string += str(m[i]) + "\n"
    return string


print(matrix_to_string(matrix))