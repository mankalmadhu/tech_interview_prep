"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/arrays/majority_elem_in_arr.py until you're done.

Problem (Majority Element, LeetCode 169):

Given an array nums of size n, return the majority element. The
majority element is the element that appears more than floor(n/2)
times. You may assume the majority element always exists.

Example:
  nums = [2, 2, 1, 1, 1, 2, 2]
  output = 2

Write your solution below.
"""


def majority_element(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num

        if candidate == num:
            count +=1
        else:
            count -=1

    return candidate


def brute_force_majority(nums):
    from collections import Counter
    counts = Counter(nums)
    n = len(nums)
    for val, c in counts.items():
        if c > n // 2:
            return val
    return None


if __name__ == "__main__":
    print(majority_element([2, 2, 1, 1, 1, 2, 2]))  # expect 2
    print(majority_element([3, 2, 3]))  # expect 3
    print(majority_element([1]))  # expect 1

    import random

    for trial in range(300):
        n = random.randint(1, 50)
        majority_val = random.randint(-5, 5)
        half = n // 2 + 1
        arr = [majority_val] * half
        arr += [random.randint(-5, 5) for _ in range(n - half)]
        random.shuffle(arr)

        got = majority_element(arr)
        expected = brute_force_majority(arr)
        assert got == expected, f"Mismatch on {arr}: got {got}, expected {expected}"

    print("All stress tests passed!")
