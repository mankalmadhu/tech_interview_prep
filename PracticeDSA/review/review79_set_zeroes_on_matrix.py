"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/arrays/set_zeroes-on_matrix.py until you're done.

Problem (Set Matrix Zeroes):

Given an M x N matrix A, if an element is 0, set its entire row and
column to 0. Do it in-place.

Example:
  A = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
  ]
  Output:
  [
    [1, 0, 1],
    [0, 0, 0],
    [1, 0, 1],
  ]

Write your solution below.
"""


def set_zeroes(A):
    m = len(A)
    n = len(A[0])

    fc_zero, fr_zero = False, False

    for i in range(m):
       for j in range(n):
           if A[i][j] == 0:
               if i == 0:
                   fr_zero = True
               if j == 0:
                   fc_zero = True
               if i>0 and j>0:
                   A[i][0] = 0
                   A[0][j] = 0

    for i in range(1,m):
        for j in range(1,n):
            if A[i][0] == 0 or A[0][j] == 0:
                A[i][j] = 0

    if fr_zero:
        A[0] = [0] * n

    if fc_zero:
        for i in range(m):
            A[i][0] = 0



    return A



if __name__ == "__main__":
    import copy

    A1 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
    ]
    expected1 = [
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1],
    ]
    set_zeroes(A1)
    assert A1 == expected1, A1

    A2 = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5],
    ]
    expected2 = [
        [0, 0, 0, 0],
        [0, 4, 5, 0],
        [0, 3, 1, 0],
    ]
    set_zeroes(A2)
    assert A2 == expected2, A2

    A3 = [[1, 2], [3, 4]]
    expected3 = [[1, 2], [3, 4]]
    set_zeroes(A3)
    assert A3 == expected3, A3

    print("All tests passed!")

    # Stress test: compare against independent brute-force (set-based) version
    import random

    def brute_force(A):
        m = len(A)
        n = len(A[0])
        rows, cols = set(), set()
        for i in range(m):
            for j in range(n):
                if A[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    A[i][j] = 0
        return A

    for trial in range(300):
        m = random.randint(1, 6)
        n = random.randint(1, 6)
        A = [[random.randint(0, 3) for _ in range(n)] for _ in range(m)]
        A_copy = [row[:] for row in A]
        got = set_zeroes(A)
        expected = brute_force(A_copy)
        assert got == expected, f"A={A}, got={got}, expected={expected}"

    print("Stress test passed (300 trials)!")
