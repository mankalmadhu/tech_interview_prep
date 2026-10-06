"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/arrays/suqare_sort.py until you're done.

Problem (Squares of a Sorted Array):

Given an array nums sorted in non-decreasing order (which may
contain negative numbers), return an array of the squares of each
number, also sorted in non-decreasing order.

Example:
  nums = [-4, -1, 0, 3, 10]
  output = [0, 1, 9, 16, 100]

Write your solution below. (You know the naive square+sort
approach - try the O(N) two-pointer approach instead.)
"""


def sorted_squares(nums):
    l_ptr = 0
    r_ptr = len(nums) -1
    result_ptr = len(nums) -1

    result = [0]*(len(nums))

    while l_ptr <= r_ptr:
        l_sq = nums[l_ptr] * nums[l_ptr]
        r_sq = nums[r_ptr] * nums[r_ptr]
        if l_sq > r_sq:
            result[result_ptr] = l_sq
            l_ptr += 1
        else:
            result[result_ptr] = r_sq
            r_ptr -= 1

        result_ptr -= 1

    return result



if __name__ == "__main__":
    print(sorted_squares([-4, -1, 0, 3, 10]))  # expect [0,1,9,16,100]
    print(sorted_squares([-7, -3, 2, 3, 11]))  # expect [4,9,9,49,121]
    print(sorted_squares([0]))  # expect [0]

    import random

    for trial in range(300):
        n = random.randint(1, 50)
        arr = sorted(random.randint(-30, 30) for _ in range(n))
        got = sorted_squares(arr)
        expected = sorted(x * x for x in arr)
        assert got == expected, f"Mismatch on {arr}: got {got}, expected {expected}"

    print("All stress tests passed!")
