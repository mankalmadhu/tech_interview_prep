"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/arrays/product_of_array_except_self.py until you're done.

Problem (Product of Array Except Self, LeetCode 238):

Given an integer array nums, return an array answer such that
answer[i] is equal to the product of all the elements of nums except
nums[i].

You must write an algorithm that runs in O(n) time and without using
the division operation.

Example:
  nums = [1,2,3,4]  -> [24,12,8,6]
  nums = [-1,1,0,-3,3] -> [0,0,9,0,0]

Write your solution below.
"""


def product_except_self(nums):

    n = len(nums)
    result = [1] * n

    lp = 1

    for i in range(n):
        result[i] *= lp
        lp *= nums[i]

    rp = 1
    for i in range(n - 1, -1, -1):
        result[i] *= rp
        rp *= nums[i]

    return result


if __name__ == "__main__":
    fixed_cases = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        ([2, 3], [3, 2]),
        ([5], [1]),
        ([0, 0], [0, 0]),
        ([1, 1, 1, 1], [1, 1, 1, 1]),
    ]
    for nums, expected in fixed_cases:
        got = product_except_self(nums)
        assert got == expected, f"{nums}: expected {expected}, got {got}"
    print("fixed cases passed")

    print(product_except_self([1,2,3,4]))

    import random

    def brute_force(nums):
        n = len(nums)
        result = []
        for i in range(n):
            prod = 1
            for j in range(n):
                if j != i:
                    prod *= nums[j]
            result.append(prod)
        return result

    for _ in range(1000):
        n = random.randint(1, 10)
        nums = [random.randint(-10, 10) for _ in range(n)]
        got = product_except_self(nums)
        want = brute_force(nums)
        assert got == want, f"{nums}: expected {want}, got {got}"
    print("1000 randomized trials passed")
