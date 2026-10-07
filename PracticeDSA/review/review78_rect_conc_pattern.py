"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/arrays/rect_conc_pattern.py until you're done.

Problem (Concentric Rectangles Pattern):

Given a number n, generate a (2n-1) x (2n-1) matrix where the outermost
"ring" of cells is filled with n, the next ring in is filled with n-1,
and so on down to the center cell, which is filled with 1.

Example, n=3 (5x5 matrix):
  3 3 3 3 3
  3 2 2 2 3
  3 2 1 2 3
  3 2 2 2 3
  3 3 3 3 3

Write your solution below.
"""


def generate_pattern(n):
    size = 2*n - 1

    matrix = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(size):
            distance_from_center = max(abs(i - (n - 1)), abs(j - (n - 1)))
            matrix[i][j] = 1+ distance_from_center

    return matrix

if __name__ == "__main__":
    assert generate_pattern(1) == [[1]]
    assert generate_pattern(2) == [
        [2, 2, 2],
        [2, 1, 2],
        [2, 2, 2],
    ]
    assert generate_pattern(3) == [
        [3, 3, 3, 3, 3],
        [3, 2, 2, 2, 3],
        [3, 2, 1, 2, 3],
        [3, 2, 2, 2, 3],
        [3, 3, 3, 3, 3],
    ]
    print("All tests passed!")
