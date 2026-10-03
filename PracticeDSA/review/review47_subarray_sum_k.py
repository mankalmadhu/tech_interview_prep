"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/arrays/subarray_sum_k.py until you're done.

Problem (Subarray Sum Equals K, LeetCode 560):

Given an array of integers nums and an integer k, return the total
number of subarrays whose sum equals k.

Example:
  nums = [1,1,1], k = 2
  output = 2 (subarrays: [1,1] at indices 0-1, and [1,1] at indices 1-2)

Write your solution below.
"""


def subarray_sum(nums, k):
    prefix_count = {}
    prefix_count[0] = 1

    cur_prefix = 0
    count = 0

    for num in nums:
        cur_prefix += num

        if cur_prefix - k in prefix_count:
            count += prefix_count[cur_prefix - k]

        prefix_count[cur_prefix] = prefix_count.get(cur_prefix, 0) + 1

    return count


if __name__ == "__main__":
    print(subarray_sum([1, 1, 1], 2))  # expect 2
    print(subarray_sum([1, 2, 3], 3))  # expect 2 ([1,2] and [3])
    print(subarray_sum([1], 0))  # expect 0

    assert subarray_sum([1, 1, 1], 2) == 2
    assert subarray_sum([1, 2, 3], 3) == 2
    assert subarray_sum([1], 0) == 0
    assert subarray_sum([], 0) == 0
    assert subarray_sum([-1, -1, 1], 0) == 1
    print("fixed cases passed")

    import random

    def brute_force(nums, k):
        n = len(nums)
        count = 0
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                if s == k:
                    count += 1
        return count

    for _ in range(300):
        n = random.randint(0, 15)
        nums = [random.randint(-5, 5) for _ in range(n)]
        k = random.randint(-10, 10)
        got = subarray_sum(nums, k)
        want = brute_force(nums, k)
        assert got == want, f"nums={nums}, k={k}: expected {want}, got {got}"
    print("300 randomized trials passed")
