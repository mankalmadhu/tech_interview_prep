def fractional_knapsack(items, capacity):

  """
        Solves the Fractional Knapsack Problem.

        Problem Context:
        ----------------
        - We have N items, each with a Value and a Weight.
        - We have a knapsack with capacity W.
        - We can take fractions of items (break them).
        - Goal: Maximize total value in the knapsack.

        Strategy: Greedy Approach (Value Density)
        -----------------------------------------
        Since we can break items, the optimal strategy is always to take the 
        "most valuable material" first.
        
        1. Calculate Density: value / weight for each item.
        2. Sort: Order items by density descending.
        3. Fill:
           - Iterate through sorted items.
           - Take the whole item if it fits.
           - If it doesn't fit, take the fraction that fills the remaining space 
             and stop (knapsack is full).

        Complexity Analysis:
        --------------------
        Time Complexity: O(N log N)
           - Dominated by sorting the items by ratio.
        Space Complexity: O(N)
           - To store the list of (ratio, weight, value) tuples.
        """
  weight_value_ratio = [(value / weight, weight, value)
                        for weight, value in items]
  weight_value_ratio_sorted = sorted(weight_value_ratio,
                                     key=lambda x: x[0],
                                     reverse=True)

  total_value = 0
  remaining_capacity = capacity

  for item in weight_value_ratio_sorted:
    if remaining_capacity > 0:
      ratio, weight, value = item
      if weight <= remaining_capacity:
        total_value += value
        remaining_capacity -= weight
      else:
        total_value += value * (remaining_capacity / weight)
        remaining_capacity = 0

  return total_value
