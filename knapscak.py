def solve_knapsack(capacity, weights, values, n):
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:    
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
                
    max_value = dp[n][capacity]
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):      
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i - 1)  
            w -= weights[i-1]
    selected_items.reverse()   
    return max_value, selected_items
def main():
    print("--- 0-1 Knapsack Problem Solver ---")
    try:
        n = int(input("Enter the total number of items: "))
        if n <= 0:
            print("Number of items must be greater than 0.")
            return
        weights = []
        values = []
        print("\nEnter the weight and value for each item:")
        for i in range(n):
            item_input = input(f"Item {i+1} (Format: weight value, e.g., '10 60'): ").split()
            weights.append(int(item_input[0]))
            values.append(int(item_input[1]))
        capacity = int(input("\nEnter the maximum weight capacity of the knapsack: "))
        if capacity < 0:
            print("Capacity cannot be negative.")
            return
        max_val, items_chosen = solve_knapsack(capacity, weights, values, n)

        # Print results
        print("\n================ RESULTS ================")
        print(f"Maximum Value Possible: {max_val}")
        print("Selected Items:")
        for index in items_chosen:
            print(f" -> Item {index+1} (Weight: {weights[index]}, Value: {values[index]})")
        print("=========================================")

    except (ValueError, IndexError):
        print("\nInvalid input! Please enter integers in the correct format.")
if __name__ == "__main__":
    main()

