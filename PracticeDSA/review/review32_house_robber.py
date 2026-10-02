"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/dp/house_robber.py until you're done.

Problem (House Robber, LeetCode 198):

You are a robber planning to rob houses along a street. Each house
has a certain amount of money. You cannot rob two adjacent houses
(alarm triggers). Return the maximum amount you can rob.

Recurrence: dp[i] = max(dp[i-1], nums[i] + dp[i-2])

Example:
  nums = [1,2,3,1]   -> 4  (rob house 0 and 2: 1+3=4)
  nums = [2,7,9,3,1]  -> 12 (rob house 0, 2, 4: 2+9+1=12)

Write your solution below (O(N) time, O(1) space using rolling variables).
"""


def rob(nums):
    rob1, rob2 = 0, 0

    for n in nums:
        rob1, rob2 = rob2, max(n+ rob1, rob2)

    return rob2

def rob_full_dp(nums):


    if len(nums) ==0:
        return 0

    if len(nums) ==1:
        return nums[0]

    dp = [0]*len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], nums[i]+ dp[i-2])

    return dp[-1]


if __name__ == "__main__":
    fixed_cases = [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([0], 0),
        ([], 0),
        ([2, 1, 1, 2], 4),
        ([5, 5, 10, 100, 10, 5], 110),
    ]
    for nums, expected in fixed_cases:
        got = rob(nums)
        assert got == expected, f"{nums}: expected {expected}, got {got}"
    print("fixed cases passed")

    print(rob_full_dp([1,2,3,1]))

    import random
    from functools import lru_cache

    def brute_force(nums):
        n = len(nums)

        @lru_cache(maxsize=None)
        def helper(i):
            if i >= n:
                return 0
            return max(helper(i + 1), nums[i] + helper(i + 2))

        return helper(0)

    for _ in range(1000):
        n = random.randint(0, 15)
        nums = [random.randint(0, 50) for _ in range(n)]
        got = rob(nums)
        want = brute_force(nums)
        assert got == want, f"{nums}: expected {want}, got {got}"
    print("1000 randomized trials passed")
