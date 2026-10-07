"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/arrays/missing_positive_int.py until you're done.

Problem (First Missing Positive):

Given an unsorted integer array A (may contain negatives, zeros,
duplicates, out-of-range values), find the smallest missing positive
integer. Must run in O(N) time and use O(1) extra space.

Example:
  A = [3, 4, -1, 1]
  Output: 2

  A = [1, 2, 0]
  Output: 3

  A = [7, 8, 9, 11, 12]
  Output: 1

Write your solution below.
"""

def first_missing_positive(A):
    i = 0
    n = len(A)

    while i < n:
        apt_pos = A[i] -1
        if  1 <= A[i]<= n and A[i] != A[apt_pos]:
            A[i],A[apt_pos] = A[apt_pos],A[i]
        else:
            i += 1


    for i in range(n):
        if i+1 != A[i]:
            return i+1

    return n+1


if __name__ == "__main__":
    inputs = [
        [3, 4, -1, 1],
        [1, 2, 0],
        [7, 8, 9, 11, 12],
        [4, 2, 1, 5, 8],
        [],
        [1],
        [2],
    ]
    expected_outputs = [2, 3, 1, 3, 1, 2, 1]

    for idx, A in enumerate(inputs):
        result = first_missing_positive(A)
        assert result == expected_outputs[idx], (
            f"A={A}: expected {expected_outputs[idx]}, got {result}"
        )
        print(f"Expected Result: {expected_outputs[idx]}. Actual Result: {result}")
    print("All example tests passed!")

    import random

    def brute_force(A):
        present = set(x for x in A if x > 0)
        i = 1
        while i in present:
            i += 1
        return i

    for trial in range(300):
        n = random.randint(0, 15)
        A = [random.randint(-10, 15) for _ in range(n)]
        got = first_missing_positive(A[:])
        expected = brute_force(A[:])
        assert got == expected, f"Mismatch on {A}: got {got}, expected {expected}"

    print("All stress tests passed!")
