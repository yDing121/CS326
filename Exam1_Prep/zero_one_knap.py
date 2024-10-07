def knapsack(weights, values, capacity):
    n = len(values)

    # Create a 2D array to store the maximum value at each n and capacity
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Fill the dp array
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # The maximum value is in the bottom-right corner of the dp array
    max_value = dp[n][capacity]

    # Backtrack to find the items that make up this maximum value
    w = capacity
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:  # This item was included
            selected_items.append(i - 1)  # Store index of included item
            w -= weights[i - 1]  # Reduce the weight

    return max_value, selected_items

if __name__ == '__main__':
    # Example usage
    weights = [10,20,30]
    values = [60, 100, 120]
    capacity = 50

    max_value, selected_items = knapsack(weights, values, capacity)
    print(f"Maximum value: {max_value}")
    print(f"Selected items (indices): {selected_items}")
