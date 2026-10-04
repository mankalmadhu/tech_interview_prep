"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/math/is_rectangle.py until you're done.

Problem (Is Rectangle):

Given four integers A, B, C, D representing the lengths of four
sides (in some order) of a quadrilateral, determine if they could
form a rectangle (opposite sides equal in pairs). Return 1 if yes,
0 otherwise.

Example:
  A=5, B=5, C=5, D=5 -> output = 1  (square is a rectangle)
  A=2, B=3, C=2, D=3 -> output = 1
  A=2, B=3, C=3, D=4 -> output = 0

Write your solution below.
"""


def is_rectangle(A, B, C, D):
    return 1 if ((A == B == C == D) or ( A == C and B == D) or (A == B and C == D) or ( A == D and B == C))else 0


def brute_force_is_rectangle(A, B, C, D):
    from collections import Counter
    sides = [A, B, C, D]
    counts = sorted(Counter(sides).values(), reverse=True)
    # valid: all 4 same (square), or two distinct pairs of 2
    return 1 if counts in ([4], [2, 2]) else 0


if __name__ == "__main__":
    print(is_rectangle(5, 5, 5, 5))  # expect 1
    print(is_rectangle(2, 3, 2, 3))  # expect 1
    print(is_rectangle(2, 3, 3, 4))  # expect 0
    print(is_rectangle(2, 3, 3, 2))  # expect 1

    import random
    import itertools

    for trial in range(300):
        sides = [random.randint(1, 5) for _ in range(4)]
        for perm in itertools.permutations(sides):
            A, B, C, D = perm
            got = is_rectangle(A, B, C, D)
            expected = brute_force_is_rectangle(A, B, C, D)
            assert got == expected, f"Mismatch on {perm}: got {got}, expected {expected}"

    print("All stress tests passed!")
