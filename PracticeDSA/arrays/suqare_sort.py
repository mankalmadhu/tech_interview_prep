class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        A_square = [elem * elem for elem in A]
        A_square.sort()
        return A_square


"""
Optimal O(N) Two Pointer Solution:
Discussion & Logic:
- Since the array is already sorted in non-decreasing order but contains negatives, the largest absolute values (and therefore the largest squares) will always be at the far left or far right edges of the array.
- We can use two pointers (`left` at the start, `right` at the end) and compare their squares.
- We initialize a `result` array of size N. Since we are finding the *largest* squares first, we must populate this result array from right-to-left (back to front) to ensure the final array is sorted in ascending order.
- Whichever pointer has the larger square gets placed at the current back index of the result array, and that pointer moves inward.

Complexity Analysis:
- Time Complexity: O(N) where N is the number of elements. We iterate through the array exactly once with the two pointers.
- Space Complexity: O(N) strictly for the auxiliary `result` array required to hold the answers.
"""


class SolutionOptimal:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n

        left, right, res_index = 0, n - 1, n - 1

        while left <= right:
            l_squared = nums[left] * nums[left]
            r_squared = nums[right] * nums[right]

            if l_squared > r_squared:
                result[res_index] = l_squared
                left += 1
            else:
                result[res_index] = r_squared
                right -= 1

            res_index -= 1
        return result


def _brute_force_sorted_squares(nums):
    return sorted(x * x for x in nums)


if __name__ == "__main__":
    sol = Solution()
    opt = SolutionOptimal()
    print(sol.solve([-4, -1, 0, 3, 10]))
    print(opt.sortedSquares([-4, -1, 0, 3, 10]))  # expect [0,1,9,16,100]

    import random

    for trial in range(300):
        n = random.randint(1, 50)
        arr = sorted(random.randint(-30, 30) for _ in range(n))
        expected = _brute_force_sorted_squares(arr)
        assert sol.solve(arr) == expected, f"Solution mismatch on {arr}"
        assert opt.sortedSquares(arr) == expected, f"SolutionOptimal mismatch on {arr}"

    print("All stress tests passed!")
