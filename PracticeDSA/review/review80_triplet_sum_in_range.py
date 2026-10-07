"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/arrays/triplet_sum_in_range.py until you're done.

Problem (Triplets With Sum Between Given Range):

https://www.interviewbit.com/problems/triplets-with-sum-between-given-range/

Given an array of real numbers A (as strings), determine whether there
exists a triplet (a, b, c) such that 1 < a + b + c < 2.

Return 1 if such a triplet exists, else 0.

Example:
  A = ["0.6", "0.7", "0.8", "1.2", "0.4"]
  Output: 1  (e.g. 0.6 + 0.7 + 0.4 = 1.7, in range)

Note: per prior review discussion, only the two-pointer approach is
being reviewed here (not the bucket-based one in the original file).

Write your solution below.
"""


def triplet_in_range(A):
    sum = 0
    A = sorted([float(s) for s in A])

    for i in range(len(A)):
        left = i+1
        right = len(A) -1
        while left < right:
            sum = A[left] + A[i] + A[right]

            if sum >1 and sum <2:
                return 1

            if sum <=1:
                left += 1
            else:
                right -= 1

    return 0


if __name__ == "__main__":
    assert triplet_in_range(["0.6", "0.7", "0.8", "1.2", "0.4"]) == 1
    assert triplet_in_range(["0.1", "0.2", "0.3", "0.4"]) == 0
    assert triplet_in_range(["0.8", "0.7", "0.9"]) == 0
    assert triplet_in_range(["0.1", "0.8", "0.25", "1.5"]) == 1
    assert triplet_in_range(["0.2", "0.3", "2.5", "3.0"]) == 0
    assert triplet_in_range(["1.1", "0.5"]) == 0
    assert (
        triplet_in_range(
            [
                "2.673662",
                "2.419159",
                "0.573816",
                "2.454376",
                "0.403605",
                "2.503658",
                "0.806191",
            ]
        )
        == 1
    )
    print("All tests passed!")

    # Stress test: compare against independent brute-force O(N^3) check
    import random
    from itertools import combinations

    def brute_force(A):
        nums = [float(s) for s in A]
        for a, b, c in combinations(nums, 3):
            s = a + b + c
            if 1 < s < 2:
                return 1
        return 0

    for trial in range(300):
        n = random.randint(3, 8)
        A = [f"{random.uniform(0, 3):.4f}" for _ in range(n)]
        expected = brute_force(A)
        got = triplet_in_range(A)
        assert got == expected, f"A={A}, got={got}, expected={expected}"

    print("Stress test passed (300 trials vs brute force)!")
