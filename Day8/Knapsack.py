def fractional_knapsack(W, weights, values, N):
    # Create a list of items with value-to-weight ratio
    items = []
    for i in range(N):
        ratio = values[i] / weights[i]
        items.append((ratio, values[i], weights[i]))

    # Sort items by ratio in descending order
    items.sort(reverse=True)

    total_value = 0.0

    for ratio, value, weight in items:
        if W == 0:
            break
        if weight <= W:
            total_value += value
            W -= weight
        else:
            total_value += ratio * W
            W = 0

    return round(total_value, 2)

# Example usage:
N = 3
W = 50
values = [100, 60, 120]
weights = [20, 10, 30]

max_value = fractional_knapsack(W, weights, values, N)
print("Maximum value in knapsack:", max_value)
#time O(N)+O(NlogN)+log(N)
#space O(N)