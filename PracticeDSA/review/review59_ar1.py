"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/arrays/ar1.py until you're done.

Problem (Array Row Reversal):

Given a 2D matrix A (list of rows), reverse each row and return
a new matrix B (do not mutate A in place — build a new matrix).

Example:
  A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
  output = [[4, 3, 2, 1], [8, 7, 6, 5], [12, 11, 10, 9]]

Write your solution below.
"""


def reverse_rows(A):
    out = []
    m = len(A)

    for i in range(m):
        n = len(A[i])
        out.append([0]*n)
        for j in range(n):
            out[i][n-j-1] = A[i][j]

    return out


if __name__ == "__main__":
    A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(reverse_rows(A))
    # expect [[4,3,2,1],[8,7,6,5],[12,11,10,9]]

    import random

    for trial in range(300):
        m = random.randint(1, 10)
        A = [[random.randint(-20, 20) for _ in range(random.randint(0, 8))] for _ in range(m)]
        expected = [row[::-1] for row in A]
        got = reverse_rows(A)
        assert got == expected, f"Mismatch on {A}: got {got}, expected {expected}"

    print("All stress tests passed!")
