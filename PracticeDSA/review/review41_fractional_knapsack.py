"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/greedy_algo/knapsack_weight_value.py until you're done.

Problem (Fractional Knapsack):

You have N items, each with a value and a weight. You have a
knapsack with capacity W. Unlike 0/1 Knapsack, you CAN take
fractions of an item (e.g., half of an item, giving half its value
and half its weight).

Maximize the total value you can carry without exceeding capacity.

Example:
  items = [(value=60, weight=10), (value=100, weight=20), (value=120, weight=30)]
  capacity = 50
  -> 240.0
  (take item1 fully: 60, item2 fully: 100, then 2/3 of item3: 80 -> total 240)

Write your solution below.
"""


def fractional_knapsack(items, capacity):
    weight_value_ratio = [(value / weight, weight, value) for value, weight in items]
    weight_value_ratio_sorted = sorted(
        weight_value_ratio, key=lambda x: x[0], reverse=True
    )

    total_value = 0

    for item in weight_value_ratio_sorted:
        _, weight, value = item
        if weight <= capacity:
            total_value += value
            capacity -= weight
        else:
            total_value += (capacity/weight)*value
            capacity = 0
    return total_value




if __name__ == "__main__":
    fixed_cases = [
        ([(60, 10), (100, 20), (120, 30)], 50, 240.0),
        ([(60, 10), (100, 20), (120, 30)], 0, 0.0),
        ([(60, 10), (100, 20), (120, 30)], 100, 280.0),
        ([(10, 5)], 10, 10.0),
        ([(10, 5)], 2, 4.0),
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
        # Same greedy logic, independently re-derived for cross-check.
        sorted_items = sorted(items, key=lambda iv: iv[0] / iv[1], reverse=True)
        total = 0.0
        remaining = capacity
        for value, weight in sorted_items:
            if remaining <= 0:
                break
            take_weight = min(weight, remaining)
            total += (take_weight / weight) * value
            remaining -= take_weight
        return total

    for _ in range(300):
        n = random.randint(0, 8)
        items = [
            (random.randint(1, 100), random.randint(1, 20)) for _ in range(n)
        ]
        capacity = random.randint(0, 100)
        got = fractional_knapsack(items, capacity)
        want = brute_force_fractional(items, capacity)
        assert abs(got - want) < 1e-6, f"{items},{capacity}: expected {want}, got {got}"
    print("300 randomized trials passed")
