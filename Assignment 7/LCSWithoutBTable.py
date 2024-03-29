def print_lcs(C, X, Y, i, j):
    if C[i][j] == 0:
        return ""
    if C[i][j] == C[i - 1][j - 1] + 1:
        return print_lcs(C, X, Y, i - 1, j - 1) + X[i - 1]
    elif C[i][j] == C[i - 1][j]:
        return print_lcs(C, X, Y, i - 1, j)
    else:
        return print_lcs(C, X, Y, i, j - 1)

# Example usage:
def lcs_length_with_tables(X, Y):
    m = len(X)
    n = len(Y)

    # Initialize the tables to store the lengths of LCS and backtrack pointers
    C = [[0] * (n + 1) for _ in range(m + 1)]  # Table for lengths of LCS
    B = [[""] * (n + 1) for _ in range(m + 1)]  # Table for backtrack pointers

    # Build the LCS table bottom-up
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                C[i][j] = C[i - 1][j - 1] + 1
                B[i][j] = "↖"  # Diagonal arrow indicating a match
            else:
                if C[i - 1][j] >= C[i][j - 1]:
                    C[i][j] = C[i - 1][j]
                    B[i][j] = "↑"  # Up arrow indicating backtrack to above cell
                else:
                    C[i][j] = C[i][j - 1]
                    B[i][j] = "←"  # Left arrow indicating backtrack to left cell

    return C, B

X = "AGGTAB"
Y = "GXTXAYB"
C, B = lcs_length_with_tables(X, Y)

# Find length of LCS
lcs_length = C[len(X)][len(Y)]
print("Length of LCS:", lcs_length)

# Print LCS
print("LCS:", print_lcs(C, X, Y, len(X), len(Y)))