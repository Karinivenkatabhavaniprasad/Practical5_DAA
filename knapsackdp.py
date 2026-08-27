def solve_knapsack(weights, values, capacity, n):
    # Initialize a 2D DP table with zeros
    # Rows represent items (0 to n), columns represent capacities (0 to capacity)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Build the table in a bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # Maximize by either taking the item or leaving it
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                # Item is too heavy, skip it
                dp[i][w] = dp[i - 1][w]
                
    # Record the maximum value
    max_value = dp[n][capacity]
    
    # Backtrack to find the specific items selected
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        # If the value changed from the row above, the item was included
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)  # Store 0-based index
            w -= weights[i - 1]
            
    # Reverse to keep sequential order
    selected_items.reverse()
    
    return max_value, selected_items


def main():
    print("--- Dynamic 0/1 Knapsack Solver ---")
    try:
        # Step 1: Get overall knapsack capacity
        capacity = int(input("Enter the maximum weight capacity of the knapsack: "))
        if capacity < 0:
            print("Capacity cannot be negative.")
            return

        # Step 2: Get total number of items
        n = int(input("Enter the total number of items available: "))
        if n <= 0:
            print("Number of items must be greater than zero.")
            return

        weights = []
        values = []

        # Step 3: Loop dynamically to gather weight and value for each item
        print("\nEnter the weight and value for each item:")
        for i in range(n):
            print(f"\nItem {i + 1}:")
            w = int(input(f"  Weight: "))
            v = int(input(f"  Value/Profit: "))
            weights.append(w)
            values.append(v)

        # Step 4: Compute the results
        max_value, selected_indices = solve_knapsack(weights, values, capacity, n)

        # Step 5: Output results clearly
        print("\n" + "="*30)
        print("RESULTS")
        print("="*30)
        print(f"Maximum Value Achieved: {max_value}")
        print(f"Selected Items (1-based index): {[idx + 1 for idx in selected_indices]}")
        print(f"Weights of Selected Items: {[weights[idx] for idx in selected_indices]}")
        print(f"Values of Selected Items: {[values[idx] for idx in selected_indices]}")
        print(f"Total Weight Used: {sum(weights[idx] for idx in selected_indices)} / {capacity}")

    except ValueError:
        print("\nInvalid input! Please ensure you enter integers for capacities, weights, and values.")


if __name__ == "__main__":
    main()
