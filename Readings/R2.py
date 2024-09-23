def min_break_cost(n, L):
    # Adding 0 (start) and n (end) to the break points list
    L = [0] + L + [n]
    m = len(L)

    # dp[i][j] will hold the minimum cost to break the string from L[i] to L[j]
    dp = [[0] * m for _ in range(m)]

    # Fill the dp table
    for length in range(2, m):  # length is the distance between i and j
        for i in range(m - length):
            j = i + length
            dp[i][j] = float('inf')  # Initialize to a large number
            for k in range(i + 1, j):
                # cost to break at k
                cost = L[j] - L[i] + dp[i][k] + dp[k][j]
                # Find the minimum cost
                dp[i][j] = min(dp[i][j], cost)

    # The answer is the minimum cost to break the entire string from 0 to n
    return dp[0][m - 1]


# Example usage
n = 20  # Length of the string
L = [2, 8, 10]  # Positions where breaks need to be made

min_cost = min_break_cost(n, L)
print(f"Minimum cost of breaking the string: {min_cost}")
