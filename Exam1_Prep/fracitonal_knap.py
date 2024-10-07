def fractional_knapsack(weights, values, capacity):
    # Calculate value-to-weight ratio and store items with their index
    items = [(values[i] / weights[i], weights[i], values[i], i) for i in range(len(weights))]

    # Sort items by ratio in descending order
    items.sort(key=lambda x: x[0], reverse=True)

    total_value = 0  # Total value accumulated
    remaining_capacity = capacity  # Remaining capacity of the knapsack
    selected_items = []  # To keep track of selected items and their fractions

    for ratio, weight, value, index in items:
        if remaining_capacity >= weight:
            # If the entire item can be taken
            total_value += value
            remaining_capacity -= weight
            selected_items.append((index, 1.0))  # Add item index with full weight (1.0)
        else:
            # If only a fraction of the item can be taken
            fraction = remaining_capacity / weight
            total_value += value * fraction
            selected_items.append((index, fraction))  # Add item index with fractional weight
            break  # Knapsack is full

    return total_value, selected_items


if __name__ == '__main__':
    # Example usage:
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    max_value, selected_items = fractional_knapsack(weights, values, capacity)

    print(f"Maximum value in the knapsack: {max_value}")
    print("Selected items (index, fraction):", selected_items)
