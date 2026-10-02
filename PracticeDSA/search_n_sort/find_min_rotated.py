from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Finds the minimum element in a sorted array that has been rotated.
        Time Complexity: O(log N) on average, O(N) worst case if there are many duplicates.
        Space Complexity: O(1) auxiliary space.

        The Logic:
        - If nums[left] < nums[right], the array is already perfectly sorted, return nums[left].
        - Use Binary Search to find the rotation point (the "cliff"):
          - If nums[mid] > nums[right]: The sequence drops off somewhere to the right.
            The minimum must be in the right half -> `left = mid + 1`.
          - If nums[mid] < nums[right]: The right half is perfectly sorted, so the
            minimum must be at mid or in the left half -> `right = mid`.
          - If nums[mid] == nums[right]: We cannot be sure which half the minimum is in.
            We safely discard the duplicate at the end by shrinking `right -= 1`.
        """

        left, right = 0, len(nums) - 1

        if nums[left] < nums[right]:
            return nums[left]

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1  # handles duplicates

        return nums[
            left
        ]  # thanks to while loop left == right at the end, so we can return either


if __name__ == "__main__":
    sol = Solution()
    print(
        "Test 1: [3,4,5,1,2]       -> Expected: 1,  Got:", sol.findMin([3, 4, 5, 1, 2])
    )
    print(
        "Test 2: [4,5,6,7,0,1,2]   -> Expected: 0,  Got:",
        sol.findMin([4, 5, 6, 7, 0, 1, 2]),
    )
    print(
        "Test 3: [11,13,15,17]     -> Expected: 11, Got:", sol.findMin([11, 13, 15, 17])
    )
    print("Test 4: [2,1]             -> Expected: 1,  Got:", sol.findMin([2, 1]))
    print("Test 5: [1]               -> Expected: 1,  Got:", sol.findMin([1]))
    print("All tests executed!")

    fixed_cases = [
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([11, 13, 15, 17], 11),
        ([2, 1], 1),
        ([1], 1),
        ([5, 1, 2, 3, 4], 1),
    ]
    for nums, expected in fixed_cases:
        got = sol.findMin(nums)
        assert got == expected, f"{nums}: expected {expected}, got {got}"
    print("fixed cases passed")

    import random

    for _ in range(1000):
        n = random.randint(1, 15)
        base = sorted(random.sample(range(-50, 50), n))
        rotation = random.randint(0, n - 1)
        rotated = base[rotation:] + base[:rotation]
        got = sol.findMin(rotated)
        want = min(base)
        assert got == want, f"{rotated}: expected {want}, got {got}"
    print("1000 randomized trials passed")
