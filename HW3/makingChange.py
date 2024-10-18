def min_coins(coins, n):
    # Initialize DP array
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # Base case: 0 coins for value 0
    backtrack = [-1] * (n+1)

    # Iterate over all values from 1 to n
    for i in range(1, n + 1):
        # Try each coin denomination
        for coin in coins:
            if i - coin >= 0 and dp[i-coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                backtrack[i] = coin

    return dp[n], backtrack

def bc(backtrack, n):
    r = n

    while r > 0:
        print(backtrack[r], end=" ")
        r -= backtrack[r]

if __name__ == '__main__':
    n = 63
    coins = [25, 10, 1]
    res, backtrack = min_coins(coins, n)
    print(res)
    bc(backtrack, n)