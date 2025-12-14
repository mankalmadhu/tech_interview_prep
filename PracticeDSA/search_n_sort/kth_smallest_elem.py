#https://www.interviewbit.com/problems/kth-smallest-element-in-the-array/
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        """
        Finds the B-th smallest element in the array.

        Strategy: Binary Search on Answer (Value Range)
        -----------------------------------------------
        Instead of sorting the array (which takes O(N log N)), we search the 
        range of possible values [min(A), max(A)].

        1. Range Definition:
           - Low = min(A), High = max(A).
        
        2. The Search Loop:
           - Pick a candidate value 'mid'.
           - Count how many numbers in A are less than or equal to 'mid'.
           - Decision:
             - If count < B: 'mid' is too small. We need more numbers. 
               Move low to mid + 1.
             - If count >= B: 'mid' is large enough to cover the B-th rank. 
               It could be the answer, or the answer is smaller. 
               Move high to mid (keep mid as a candidate).

        Complexity Analysis:
        --------------------
        Time Complexity: O(N * log(max(A) - min(A)))
           - The search space is the range of values (R). Binary search takes O(log R).
           - Each step involves a linear scan of A, taking O(N).
        
        Space Complexity: O(1)
           - No auxiliary data structures used.
        """
        low = min(A)
        high = max(A)
        while low < high:
            mid = (low+high)//2
            count = 0
            for num in A:
                if num <= mid:
                    count += 1
            if count < B:
                low = mid+1
            else:
                high = mid
        
        return low
