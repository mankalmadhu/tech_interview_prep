"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/arrays/two_sum.py until you're done.

Problem (Two Sum, LeetCode 1):

Given an array of integers nums and an integer target, return
indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and
you may not use the same element twice.

Example:
  nums = [2,7,11,15], target = 9  -> [0,1]  (2 + 7 = 9)
  nums = [3,2,4], target = 6      -> [1,2]  (2 + 4 = 6)
  nums = [3,3], target = 6        -> [0,1]

Write your solution below (aim for O(N) time).
"""


def two_sum(nums, target):
    lookup = {}

    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in lookup:
            return (lookup[diff],i)

        lookup[nums[i]] = i

    return []


if __name__ == "__main__":
    pass
