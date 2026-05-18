class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        Calculates the maximum money that can be robbed from houses in a street
        without robbing two adjacent houses.

        Algorithm: 1D Dynamic Programming (Space-Optimized)
        - Time Complexity: O(N) since we iterate through the houses exactly once.
        - Space Complexity: O(1) auxiliary space, optimized from O(N) by only 
          retaining the last two computed DP states (rob1 and rob2).

        Recurrence Relation:
        - dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        - Translated to O(1) space variables:
          rob1, rob2 = rob2, max(n + rob1, rob2)
        """
        rob1, rob2 = 0, 0
        
        for n in nums:
            rob1, rob2 = rob2, max(n + rob1, rob2)
        return rob2


if __name__ == '__main__':
    sol = Solution()
    print("Test 1: [1,2,3,1]   -> Expected: 4, Got:", sol.rob([1,2,3,1]))
    print("Test 2: [2,7,9,3,1] -> Expected: 12, Got:", sol.rob([2,7,9,3,1]))
    print("Test 3: [0]         -> Expected: 0, Got:", sol.rob([0]))
    print("Test 4: []          -> Expected: 0, Got:", sol.rob([]))
    print("Test 5: [2,1,1,2]   -> Expected: 4, Got:", sol.rob([2,1,1,2]))
    print("All tests executed!")