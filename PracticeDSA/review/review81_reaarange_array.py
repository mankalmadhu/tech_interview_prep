"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/math/reaarange_array.py until you're done.

Problem (Rearrange Array):

https://www.interviewbit.com/problems/rearrange-array/

Given an array A of size N, where every element is in range [0, N-1],
rearrange it in-place such that A[i] becomes A[A[i]] (the original
A[i]'s value is used as an index to look up the final value for
position i). Must use O(1) extra space.

Example:
  A = [1, 0]
  Output: [0, 1]
  (A[0] = A[A[0]] = A[1] = 0; A[1] = A[A[1]] = A[0] = 1)

Write your solution below.
"""


def rearrange(A):
    n = len(A)
    for i in range(n):
        A[i] = A[i] + (A[A[i]] %n )*n

    for i in range(n):
        A[i] = A[i]//n


if __name__ == "__main__":
    A1 = [1, 0]
    rearrange(A1)
    assert A1 == [0, 1], A1

    A2 = [2, 0, 1]
    rearrange(A2)
    assert A2 == [1, 2, 0], A2

    A3 = [0]
    rearrange(A3)
    assert A3 == [0], A3

    A4 = [3, 2, 1, 0]
    rearrange(A4)
    assert A4 == [0, 1, 2, 3], A4

    print("All tests passed!")

    # Stress test: compare against independent brute-force (temp copy) version
    import random

    def brute_force(A):
        n = len(A)
        orig = A[:]
        return [orig[orig[i]] for i in range(n)]

    for trial in range(300):
        n = random.randint(1, 10)
        perm = list(range(n))
        random.shuffle(perm)
        expected = brute_force(perm)
        got = perm[:]
        rearrange(got)
        assert got == expected, f"A={perm}, got={got}, expected={expected}"

    print("Stress test passed (300 trials)!")
