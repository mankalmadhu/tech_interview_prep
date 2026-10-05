"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/arrays/pick_both_sides.py until you're done.

Problem (Pick From Both Sides):

https://www.interviewbit.com/problems/pick-from-both-sides/

Given an array A and an integer B, you must pick exactly B
elements total, where each pick is either from the front or the
back of the array (you can mix front/back picks in any order, but
once picked, elements are removed from that end). Maximize the
sum of the B picked elements.

Example:
  A = [5, -2, 3, 1, 2], B = 3
  Picking 2 from front (5, -2) + 1 from back (2) = 5
  Picking 1 from front (5) + 2 from back (2, 1) = 8  <- best
  output = 8

Write your solution below.
"""


def pick_both_sides(A, B):
    max_sum = 0

    if len(A) < B:
        return max_sum

    cur_sum = sum(A[0:B])
    max_sum = cur_sum
    n = len(A)

    for i in range(B):
        cur_sum -= A[B-i-1]
        cur_sum  += A[n-i-1]
        max_sum = max(max_sum, cur_sum)

    return max_sum



if __name__ == "__main__":
    print(pick_both_sides([5, -2, 3, 1, 2], 3))  # expect 8
    print(pick_both_sides([1, 2, 3, 4, 5], 3))  # expect 12 (3+4+5)
    print(pick_both_sides([1, 1, 1, 1, 1], 5))  # expect 5

    import random

    def brute_force_pick(A, B):
        n = len(A)
        if n < B:
            return 0
        if B == 0:
            return 0
        best = None
        for k in range(B + 1):  # k from front, B-k from back
            front = sum(A[:k]) if k > 0 else 0
            back = sum(A[n - (B - k):]) if (B - k) > 0 else 0
            total = front + back
            if best is None or total > best:
                best = total
        return best

    for trial in range(300):
        n = random.randint(1, 20)
        arr = [random.randint(-10, 10) for _ in range(n)]
        B = random.randint(0, n)
        got = pick_both_sides(arr, B)
        expected = brute_force_pick(arr, B)
        assert got == expected, f"Mismatch on {arr}, B={B}: got {got}, expected {expected}"

    print("All stress tests passed!")
