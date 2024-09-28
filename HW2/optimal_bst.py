def optimalBST(P, Q):
    # Get number of keys
    n = len(P)

    # Pad P on the left to fix indexing (P starts at 1)
    P = [None] + P

    # Initialize DP arrays to the correct size
    E = [None] + [[0 for __ in range(1, n+2)] for _ in range(1, n+2)]
    W = [None] + [[0 for __ in range(1, n+2)] for _ in range(1, n+2)]
    ROOT = [[None for _ in range(n)]] + [([None] + [0 for _ in range(n)]) for __ in range(n)]

    # Base cases
    for i in range(1, n+2):
        E[i][i-1] = Q[i-1]
        W[i][i-1] = Q[i-1]

    for l in range(1, n+1):
        for i in range(1, n-l + 2):
            j = i + l - 1
            E[i][j] = float("inf")
            W[i][j] = W[i][j-1] + P[j] + Q[j]

            # Find root
            for r in range(i, j+1):
                t = E[i][r-1] + E[r+1][j] + W[i][j]
                if t < E[i][j]:
                    E[i][j] = t
                    ROOT[i][j] = r

    return E, W, ROOT


if __name__ == '__main__':
    P = [0.08, 0.06, 0.07, 0.03, 0.05, 0.12, 0.1]
    Q = [0.05, 0.07, 0.03, 0.04, 0.04, 0.09, 0.09, 0.08]

    print(f"Sum of P and Q:\t{sum(P) + sum(Q)}")
    e_arr, w_arr, roots_arr = optimalBST(P, Q)

    print("---E")
    for row in e_arr:
        if type(row) == list:
            print(row[1:])

    print("---W")
    for row in w_arr:
        if type(row) == list:
            print(row[1:])

    print("---Root")
    for row in roots_arr:
        print(row)