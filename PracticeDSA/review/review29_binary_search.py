"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/search_n_sort/binary_search.py until you're done.

Problem (Binary Search, LeetCode 704):

Given a sorted array and a target value, return the index of target
if it exists, else return -1.

Write your solution below (O(log N) time, O(1) space).
"""


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1



if __name__ == "__main__":
    fixed_cases = [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
        ([], 5, -1),
        ([5], 5, 0),
        ([1, 2, 3, 4, 5], 1, 0),
        ([1, 2, 3, 4, 5], 5, 4),
    ]
    for arr, target, expected in fixed_cases:
        got = binary_search(arr, target)
        assert got == expected, f"{arr}, target={target}: expected {expected}, got {got}"
    print("fixed cases passed")

    import random
    for _ in range(1000):
        n = random.randint(0, 20)
        arr = sorted(random.sample(range(0, 200), n))
        target = random.choice(arr) if arr and random.random() < 0.5 else random.randint(0, 200)
        got = binary_search(arr, target)
        want = arr.index(target) if target in arr else -1
        assert got == want, f"{arr}, target={target}: expected {want}, got {got}"
    print("1000 randomized trials passed")
