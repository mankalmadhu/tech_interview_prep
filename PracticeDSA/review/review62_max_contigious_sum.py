"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/arrays/max_contigious_sum.py until you're done.

Problem (Maximum Subarray Sum, Kadane's Algorithm):

https://www.interviewbit.com/problems/max-sum-contiguous-subarray/

Given an array of integers A, find the contiguous subarray
(containing at least one number) which has the largest sum, and
return that sum.

Example:
  A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
  output = 6  (subarray [4, -1, 2, 1])

Write your solution below.
"""


def max_subarray_sum(A):
    if not A:
        return 0

    max_sum , cur_sum = A[0], A[0]

    for i in range(1, len(A)):
        cur_sum = max(A[i], A[i] + cur_sum)
        max_sum = max(cur_sum, max_sum)

    return max_sum


if __name__ == "__main__":
    print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # expect 6
    print(max_subarray_sum([1]))  # expect 1
    print(max_subarray_sum([-1, -2, -3]))  # expect -1 (all negative)
    print(max_subarray_sum([1, 2, -5, 4]))  # expect 4

    import random

    def brute_force_max_subarray(A):
        best = A[0]
        for i in range(len(A)):
            cur = 0
            for j in range(i, len(A)):
                cur += A[j]
                best = max(best, cur)
        return best

    for trial in range(300):
        n = random.randint(1, 50)
        arr = [random.randint(-20, 20) for _ in range(n)]
        got = max_subarray_sum(arr)
        expected = brute_force_max_subarray(arr)
        assert got == expected, f"Mismatch on {arr}: got {got}, expected {expected}"

    print("All stress tests passed!")
