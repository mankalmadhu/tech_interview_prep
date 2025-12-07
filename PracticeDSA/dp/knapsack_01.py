
"""
The Setup
values: [10, 40, 30]

weights: [5, 4, 6]

capacity: 8

n: 3

We want to find the result of knapsack_helper(values, weights, 8, 3, memo). Let's use K(n, c) as a shorthand for this function call. Our goal is to find K(3, 8).

The memo table is a 2D array of size 4x9, initially filled with -1. memo[n][c] will store the result of K(n, c).

The Trace (A Recursive Journey)
Here's how the calls will unfold. I'll use indentation to show the recursion depth.

1. K(3, 8) is called. (Considering [10, 40, 30], capacity 8)

Item 3 (value=30, weight=6) fits. We need to find the max of two choices:

Exclude Item 3: We need the result of K(2, 8).

Include Item 3: We need 30 + K(2, 8 - 6), which is 30 + K(2, 2).

2. Let's explore the "Exclude" path first: K(2, 8) (Considering [10, 40], capacity 8)

Item 2 (value=40, weight=4) fits. We need max of:

Exclude Item 2: K(1, 8)

Include Item 2: 40 + K(1, 8 - 4), which is 40 + K(1, 4).

3. Let's go deeper: K(1, 8) (Considering [10], capacity 8)

Item 1 (value=10, weight=5) fits. We need max of:

Exclude Item 1: K(0, 8). This is a base case and returns 0.

Include Item 1: 10 + K(0, 8 - 5), which is 10 + K(0, 3). This is also a base case (10 + 0 = 10).

The result is max(0, 10) = 10.

SAVE: We store this result: memo[1][8] = 10.

4. Now back to step 2, let's explore its "Include" path: K(1, 4)

Item 1 (value=10, weight=5) is too heavy (5 > 4).

We can't include it. The result is K(0, 4). This is a base case and returns 0.

SAVE: We store this result: memo[1][4] = 0.

5. We can now resolve K(2, 8) from step 2.

The two choices were:

K(1, 8) which we found was 10.

40 + K(1, 4) which we found was 40 + 0 = 40.

The result is max(10, 40) = 40.

SAVE: We store this: memo[2][8] = 40.

The Magic of Memoization
6. Now back to our original call K(3, 8).

We have the result for the "Exclude" path: K(2, 8) = 40.

Now we need the "Include" path: 30 + K(2, 2).

7. Let's compute K(2, 2) (Considering [10, 40], capacity 2)

Item 2 (value=40, weight=4) is too heavy.

The result is K(1, 2).

K(1, 2): Item 1 (value=10, weight=5) is too heavy.

The result is K(0, 2). This is a base case and returns 0.

SAVE: So, memo[1][2] = 0. And memo[2][2] = 0.

8. We can now resolve the original call K(3, 8) from step 1.

The two choices were:

"Exclude": K(2, 8) which we found was 40.

"Include": 30 + K(2, 2) which we found was 30 + 0 = 30.

The final result is max(40, 30) = 40.

SAVE: memo[3][8] = 40.

The function returns 40. Notice how every time we computed a result for a (n, c) pair, we saved it. If any other recursive branch had needed K(1, 8), it would have instantly gotten the answer 10 from the memo table without re-computing.
"""


def knapsack_01(values, weights, capacity):
  n = len(values)
  memo = [[-1 for _ in range(capacity + 1)] for _ in range(n + 1)]
  return knapsack_01_recursive(values, weights, capacity, n, memo)


def knapsack_01_recursive(values, weights, capacity, n, memo):
  if n == 0 or capacity == 0:
    return 0

  if memo[n][capacity] != -1:
    return memo[n][capacity]

  if weights[n - 1] > capacity:
    result = knapsack_01_recursive(values, weights, capacity, n - 1, memo)
  else:
    val_exclude = knapsack_01_recursive(values, weights, capacity, n - 1, memo)
    val_include = values[n - 1] + knapsack_01_recursive(
        values, weights, capacity - weights[n - 1], n - 1, memo)
    result = max(val_exclude, val_include)

  memo[n][capacity] = result
  return result
