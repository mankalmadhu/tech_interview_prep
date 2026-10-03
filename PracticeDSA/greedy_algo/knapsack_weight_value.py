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
    weight_value_ratio = [(value / weight, weight, value) for weight, value in items]
    weight_value_ratio_sorted = sorted(
        weight_value_ratio, key=lambda x: x[0], reverse=True
    )

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


if __name__ == "__main__":
    fixed_cases = [
        ([(10, 60), (20, 100), (30, 120)], 50, 240.0),
        ([(10, 60), (20, 100), (30, 120)], 0, 0.0),
        ([(10, 60), (20, 100), (30, 120)], 100, 280.0),
        ([(5, 10)], 10, 10.0),
        ([(5, 10)], 2, 4.0),
        ([], 10, 0.0),
    ]
    for items, capacity, expected in fixed_cases:
        got = fractional_knapsack(items, capacity)
        assert abs(got - expected) < 1e-9, (
            f"{items},{capacity}: expected {expected}, got {got}"
        )
    print("fixed cases passed")

    import random

    def brute_force_fractional(items, capacity):
        sorted_items = sorted(items, key=lambda wv: wv[1] / wv[0], reverse=True)
        total = 0.0
        remaining = capacity
        for weight, value in sorted_items:
            if remaining <= 0:
                break
            take_weight = min(weight, remaining)
            total += (take_weight / weight) * value
            remaining -= take_weight
        return total

    for _ in range(300):
        n = random.randint(0, 8)
        items = [
            (random.randint(1, 20), random.randint(1, 100)) for _ in range(n)
        ]
        capacity = random.randint(0, 100)
        got = fractional_knapsack(items, capacity)
        want = brute_force_fractional(items, capacity)
        assert abs(got - want) < 1e-6, f"{items},{capacity}: expected {want}, got {got}"
    print("300 randomized trials passed")
