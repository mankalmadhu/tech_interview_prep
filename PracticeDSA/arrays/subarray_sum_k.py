from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
Given an array of integers nums and an integer k, return the total number 
        of continuous subarrays whose sum equals to k.
        
        This solution works even when the array contains negative numbers.
        
        Core Idea:
        --------------
        We use prefix sums. Let prefix[j] be the sum of elements from 0 to j.
        
        The sum of a subarray from index (i+1) to j is:
            prefix[j] - prefix[i] == k
            
        Rearranged: 
            prefix[j] - k == prefix[i]
            
        So for every position j, we check how many previous prefix sums equal 
        to (current_prefix - k). Each such match gives us valid subarrays ending at j.
        
        Why we need the hashmap:
        - It stores frequency of all prefix sums seen so far.
        - prefix_count[0] = 1 handles subarrays that start from index 0.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Example:
            nums = [1, 2, 3, -2, 3], k = 3
            Output: 4
            Subarrays: [3], [1,2], [3,-2,3], [-2,3]
        """
        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        cur_prefix = 0
        count = 0

        for num in nums:
            cur_prefix += num
            
            if cur_prefix - k in prefix_count:
                count += prefix_count[cur_prefix - k]
            
            prefix_count[cur_prefix] += 1
        
        return count
