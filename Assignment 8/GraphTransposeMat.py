def GraphTranspose_Matrix(G, GT):
    for i in range(len(G)):
        for j in range(len(G[0])):
            GT[i][j] = 0

    for i in range(len(G)):
        for j in range(len(G[0])):
                GT[j][i] = G[i][j]

# Example adjacency matrix G
G = [
    [0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1]
]

# Create a transpose matrix GT filled with zeros
GT = [[0 for _ in range(len(G))] for _ in range(len(G[0]))]

# Call the function
GraphTranspose_Matrix(G, GT)

# Print the transpose matrix GT
for row in GT:
    print(row)