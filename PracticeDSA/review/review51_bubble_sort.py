"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/search_n_sort/bubble_sort.py until you're done.

Problem (Bubble Sort):

Given an array of integers, sort it in ascending order using the
bubble sort algorithm.

Example:
  nums = [5, 2, 9, 1, 5, 6]
  output = [1, 2, 5, 5, 6, 9]

Write your solution below.
"""


def bubble_sort(nums):
    n = len(nums)

    for i in range(n):
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    return nums


if __name__ == "__main__":
    print(bubble_sort([5, 2, 9, 1, 5, 6]))  # expect [1, 2, 5, 5, 6, 9]
    print(bubble_sort([]))  # expect []
    print(bubble_sort([1]))  # expect [1]

    assert bubble_sort([5, 2, 9, 1, 5, 6]) == [1, 2, 5, 5, 6, 9]
    assert bubble_sort([]) == []
    assert bubble_sort([1]) == [1]
    assert bubble_sort([2, 1]) == [1, 2]
    assert bubble_sort([3, 3, 3]) == [3, 3, 3]
    assert bubble_sort([-5, 3, -1, 0]) == [-5, -1, 0, 3]
    print("fixed cases passed")

    import random

    for _ in range(300):
        n = random.randint(0, 50)
        nums = [random.randint(-50, 50) for _ in range(n)]
        got = bubble_sort(nums[:])
        want = sorted(nums)
        assert got == want, f"nums={nums}: expected {want}, got {got}"
    print("300 randomized trials passed")
