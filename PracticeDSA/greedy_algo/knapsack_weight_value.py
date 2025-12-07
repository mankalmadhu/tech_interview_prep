def fractional_knapsack(items, capacity):

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
