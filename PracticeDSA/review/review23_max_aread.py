"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/two_pointer/max_aread.py until you're done.

Problem (Container With Most Water, LeetCode 11):

Given an array `height` where height[i] is the height of a vertical
line at position i, find two lines that together with the x-axis form
a container holding the most water. Return the max area.

Area between lines at indices i and j (i < j) = (j - i) * min(height[i], height[j])

Example:
  height = [1,8,6,2,5,4,8,3,7] -> 49 (lines at index 1 and 8: (8-1)*min(8,7)=7*7=49)
  height = [1,1]               -> 1

Write your solution below (two-pointer, O(N) time).
"""


def calculate_max_area(height):
    lo = 0
    hi = len(height) -1
    max_area = 0

    while lo < hi:
        width = hi - lo
        length = min(height[lo], height[hi])
        if max_area < width * length:
            max_area = width * length

        if height[lo] < height[hi]:
            lo +=1
        else:
            hi -=1

    return max_area




def brute_force(height):
    n = len(height)
    best = 0
    for i in range(n):
        for j in range(i + 1, n):
            best = max(best, (j - i) * min(height[i], height[j]))
    return best


if __name__ == "__main__":
    fixed_cases = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
        ([1], 0),
        ([], 0),
    ]
    for arr, expected in fixed_cases:
        got = calculate_max_area(arr)
        assert got == expected, f"{arr}: expected {expected}, got {got}"
    print("fixed cases passed")

    import random
    for _ in range(2000):
        n = random.randint(0, 20)
        arr = [random.randint(0, 50) for _ in range(n)]
        got = calculate_max_area(arr)
        want = brute_force(arr)
        assert got == want, f"{arr}: expected {want}, got {got}"
    print("2000 randomized trials passed")
