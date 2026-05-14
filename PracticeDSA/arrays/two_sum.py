class Solution:
    """
    Finds the indices of two numbers in an array that add up to a specific target.
    
    Time Complexity: O(N)
    - We iterate through the 'nums' array exactly once.
    - Hash Map lookups and insertions are O(1) on average.
    
    Space Complexity: O(N)
    - In the worst case (no match found until the very end), the Hash Map will 
      store N-1 elements.
      
    Logic & Trade-offs:
    - We use a Hash Map (dictionary) to track numbers we've seen: {number: index}.
    - For each number, we calculate its required 'complement' (target - number).
    - If the complement is already in our map, we instantly return both indices!
    - If the array was already sorted, we could trade the O(N) space for O(1) space 
      by using the Two Pointers pattern instead of a Hash Map.
    """
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        tracker = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in tracker:
                return [tracker[diff], i]
            tracker[n] = i
        return []

if __name__ == '__main__':
    sol = Solution()
    print("Test 1: [2,7,11,15], target 9 -> Expected: [0, 1], Got:", sol.twoSum([2,7,11,15], 9))
    print("Test 2: [3,2,4], target 6     -> Expected: [1, 2], Got:", sol.twoSum([3,2,4], 6))
    print("Test 3: [3,3], target 6       -> Expected: [0, 1], Got:", sol.twoSum([3,3], 6))
    print("All tests executed!")
