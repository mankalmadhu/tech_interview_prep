"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/arrays/number_occurence.py until you're done.

Problem (Find Occurrences):

Given an array of integers A, return the count of occurrences of each
distinct number (a list/collection of counts, order doesn't matter much).

Example:
  A = [3, 1, 3, 2, 1, 1]
  Output (as counts): [3, 2, 1]  (3 occurs 3x, 1 occurs 2x, 2 occurs 1x)
  (exact order of the counts in the output isn't important here)

Write your solution below.
"""

from collections import Counter

def find_occurences(A):
    result = Counter(A)
    return sorted(result.values())


if __name__ == "__main__":
    import collections

    inputs = [[3, 1, 3, 2, 1, 1], [], [5], [1, 1, 1]]
    expected_outputs = [
        sorted([3, 2, 1]),
        [],
        [1],
        [3],
    ]

    for idx, A in enumerate(inputs):
        result = sorted(find_occurences(A))
        assert result == expected_outputs[idx], (
            f"A={A}: expected {expected_outputs[idx]}, got {result}"
        )
        print(f"Expected Result: {expected_outputs[idx]}. Actual Result: {result}")
    print("All example tests passed!")

    import random

    for trial in range(200):
        n = random.randint(0, 20)
        A = [random.randint(0, 10) for _ in range(n)]
        got = sorted(find_occurences(A))
        expected = sorted(collections.Counter(A).values())
        assert got == expected, f"Mismatch on {A}: got {got}, expected {expected}"

    print("All stress tests passed!")
