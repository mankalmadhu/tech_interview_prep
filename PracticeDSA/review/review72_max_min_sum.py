"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/arrays/max_min_sum.py until you're done.

Problem (Max Sum of Max and Min elements):

Given an array A of integers, find the sum of the maximum and minimum
elements of the array. Return 0 for an empty array.

Example:
  A = [3, 2, 1, 4]
  Output: 5   (max=4, min=1, 4+1=5)

Write your solution below.
"""


def solve(A):
    min_num = float('inf')
    max_num = float('-inf')

    if not A:
        return 0

    for i in range(len(A)):
        if A[i] < min_num:
            min_num = A[i]
        if A[i] > max_num:
            max_num = A[i]

    return min_num + max_num



if __name__ == "__main__":
    inputs = [[3, 2, 1, 4], [], [5], [-3, -1, -7, -2]]
    expected_outputs = [5, 0, 10, -8]

    for idx, A in enumerate(inputs):
        result = solve(A)
        assert result == expected_outputs[idx], (
            f"A={A}: expected {expected_outputs[idx]}, got {result}"
        )
        print(f"Expected Result: {expected_outputs[idx]}. Actual Result: {result}")
    print("All example tests passed!")

    import random

    for trial in range(300):
        n = random.randint(0, 20)
        A = [random.randint(-100, 100) for _ in range(n)]
        got = solve(A)
        expected = 0 if not A else max(A) + min(A)
        assert got == expected, f"Mismatch on {A}: got {got}, expected {expected}"

    print("All stress tests passed!")
