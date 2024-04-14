def truncate(value):
    return float(f'{value:.2f}')

def optimal_bst(p, q, n):
    e = [[0] * (n+1) for _ in range(n+2)]
    w = [[0] * (n+1) for _ in range(n+2)]
    root = [[0] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+2):
        e[i][i-1] = q[i-1]
        w[i][i-1] = q[i-1]
    
    for l in range(1, n+1):
        for i in range(1, n-l+2):
            j = i + l - 1
            e[i][j] = float('inf')
            w[i][j] = w[i][j-1] + p[j-1] + q[j]
            for r in range(i, j+1):
                t = e[i][r-1] + e[r+1][j] + w[i][j]
                if t < e[i][j]:
                    e[i][j] = t
                    root[i][j] = r
    
    for i in range(1, n+2):
        for j in range(i-1, n+1):
            e[i][j] = truncate(e[i][j])

    return e, root

# # Example usage:
# p = [0.04, 0.06, 0.08, 0.02, 0.10, 0.12, 0.14]
# q = [0.06, 0.06, 0.06, 0.06, 0.05, 0.05, 0.05, 0.05]
# n = len(p)
# e, root = optimal_bst(p, q, n)
# print("Cost table e:")
# for row in e:
#     print(row)
# print("\nRoot table:")
# for row in root:
#     print(row)

def construct_obst(keys, root, i, j, parent_key, side):
    if i <= j:
        root_key = keys[root[i][j] - 1]
        print(f"Node {root_key} is the {side} child of {parent_key}")
        construct_obst(keys, root, i, root[i][j] - 1, root_key, "left")
        construct_obst(keys, root, root[i][j] + 1, j, root_key, "right")

# Example usage:
keys = [1, 2, 3, 4, 5, 6, 7]
p = [0.04, 0.06, 0.08, 0.02, 0.10, 0.12, 0.14]
q = [0.06, 0.06, 0.06, 0.06, 0.05, 0.05, 0.05, 0.05]
n = len(p)
e, root = optimal_bst(p, q, n)
print("Cost table e:")
for row in e:
    print(row)
print("\nRoot table:")
for row in root:
    print(row)


print("Optimal Binary Search Tree structure:")
construct_obst(keys, root, 1, n, "root", "")
