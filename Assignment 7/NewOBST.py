import numpy as np
import pandas as pd

keys = [1, 2, 3, 4, 5, 6, 7]
P = [0.04, 0.06, 0.08, 0.02, 0.10, 0.12, 0.14]
Q = [0.06, 0.06, 0.06, 0.06, 0.05, 0.05, 0.05, 0.05]
n = len(P)

p = pd.Series(P, index=range(1, n+1))
q = pd.Series(Q)

e = pd.DataFrame(np.diag(Q), index=range(1, n+2))
w = pd.DataFrame(np.diag(Q), index=range(1, n+2))
root = pd.DataFrame(np.zeros((n, n)), index=range(1, n+1), columns=range(1, n+1))

for l in range(1, n+1):
    for i in range(1, n-l+2):
        j = i+l-1
        e.loc[i, j] = np.inf
        w.loc[i, j] = w.loc[i, j-1] + p[j] + q[j]
        for r in range(i, j+1):
            t = e.loc[i, r-1] + e.loc[r+1, j] + w.loc[i, j]
            if t < e.loc[i, j]:
                e.loc[i, j] = t
                root.loc[i, j] = r

print("Cost Table (e):")
print(e)

print("\nRoot Table:")
print(root)
