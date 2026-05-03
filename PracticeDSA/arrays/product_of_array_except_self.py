from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Calculates the product of array except self in O(n) time and O(1) auxiliary space.
        
        The Logic:
        Since division is not allowed, the product for index `i` is exactly the product of 
        all elements strictly to its left multiplied by all elements strictly to its right.
        Instead of allocating two separate O(n) arrays for left and right products, we do 
        this in two passes directly onto the output `result` array:
        1. Left Pass: Compute running prefix product and store it directly in `result[i]`.
        2. Right Pass: Compute running suffix product and multiply it into `result[i]`.
        
        Examples:
        Input: [1, 2, 3, 4]
        -> Output: [24, 12, 8, 6]
        
        Input: [1, 0, 3]
        -> Output: [0, 3, 0] (The logic naturally handles zeros without special cases!)
        """
        n = len(nums)
        result = [1] * n
        
        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]
        
        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
        
        return result
