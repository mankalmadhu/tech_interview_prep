"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/search_n_sort/find_min_rotated.py until you're done.

Problem (Find Minimum in Rotated Sorted Array, LeetCode 153):

Suppose an array of length n sorted in ascending order is rotated
between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7]
might become:
  [4,5,6,7,0,1,2] if it was rotated 4 times.
  [0,1,2,4,5,6,7] if it was rotated 7 times.

Given the sorted rotated array nums of unique elements, return the
minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Example:
  nums = [3,4,5,1,2]   -> 1
  nums = [4,5,6,7,0,1,2] -> 0
  nums = [11,13,15,17]  -> 11 (rotated 0 times, still sorted)

Write your solution below.
"""


def find_min(nums):
    left, right = 0, len(nums) -1

    if nums[left] < nums[right]:
        return nums[left]

    while left < right:
        mid = (left + right) //2

        if nums[mid] > nums[right]:
            left = mid +1
        else:
            right = mid

    return nums[left]


if __name__ == "__main__":
    fixed_cases = [
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([11, 13, 15, 17], 11),
        ([2, 1], 1),
        ([1], 1),
        ([5, 1, 2, 3, 4], 1),
    ]
    for nums, expected in fixed_cases:
        got = find_min(nums)
        assert got == expected, f"{nums}: expected {expected}, got {got}"
    print("fixed cases passed")

    import random

    for _ in range(1000):
        n = random.randint(1, 15)
        base = sorted(random.sample(range(-50, 50), n))
        rotation = random.randint(0, n - 1)
        rotated = base[rotation:] + base[:rotation]
        got = find_min(rotated)
        want = min(base)
        assert got == want, f"{rotated}: expected {want}, got {got}"
    print("1000 randomized trials passed")
