import numpy as np

np.set_printoptions(precision=2, suppress=True)

X = np.array(
    [
        [1,2,0],
        [0, 0, 5],
        [3, -4, 2],
        [1, 6, 5],
        [0, 1, 0],
    ]
)

U,s,W = np.linalg.svd(X)
V = W.T

D = np.zeros_like(X, dtype=float)

D[np.diag_indices(min(X.shape))] = s
print(np.dot(np.dot(U,D),V.T))
