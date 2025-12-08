#https://www.interviewbit.com/problems/even-product/
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        """
        Calculates the number of distinct operations to make the product of the array EVEN.
        
        Logic:
        1. Initial State: The problem states the initial product is ODD. This implies 
           every single number in the array is currently Odd.
        2. Target State: To make a product EVEN, we need at least one Even number 
           in the array.
        3. The Operation: We can choose *any* subset of indices and change their values.
           If we choose a non-empty subset, we can simply change those numbers to 
           Even numbers, satisfying the condition.
        
        Combinatorics:
        - For an array of size n, the total number of possible subsets of indices 
          is 2^n (the Power Set).
        - The only subset that DOES NOT work is the Empty Subset (choosing nothing), 
          because the product would remain Odd.
        - Therefore, the answer is Total Subsets - Empty Subset = (2^n) - 1.
        n=len(A)
        return ((2**n)-1)%1000000007
