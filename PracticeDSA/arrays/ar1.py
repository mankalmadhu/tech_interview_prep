"""
PROBLEM: Array Row Reversal
APPROACH: Two-pointer visualization / Direct math mapping
TIME COMPLEXITY: O(N*M) - We visit every element once.
SPACE COMPLEXITY: O(N*M) - We create a new matrix B of the same size.

CONCEPT:
The goal is to reverse each row of a 2D matrix.
Instead of swapping elements in place (which would be O(1) space but modifies input),
we create a new matrix B.

For every row `i` and column `j`:
The element `A[i][j]` moves to `B[i][n-1-j]`.
This `n-1-j` formula basically says "mirror the index across the center".
"""


def performOps(A):
    m = len(A)
    B = []
    for i in range(m):
        n = len(A[i])
        B.append([0] * n)
        for j in range(n):
            B[i][n - 1 - j] = A[i][j]
    return B


def _reverse_rows_brute(A):
    return [row[::-1] for row in A]


if __name__ == "__main__":
    A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    B = performOps(A)
    for i in range(len(B)):
        for j in range(len(B[i])):
            print(B[i][j])

    import random

    for trial in range(300):
        m = random.randint(1, 10)
        A = [[random.randint(-20, 20) for _ in range(random.randint(0, 8))] for _ in range(m)]
        expected = _reverse_rows_brute(A)
        got = performOps(A)
        assert got == expected, f"Mismatch on {A}: got {got}, expected {expected}"

    print("All stress tests passed!")
