# https://www.interviewbit.com/problems/max-sum-contiguous-subarray/
class Solution:
  # @param A : tuple of integers
  # @return an integer
  def maxSubArray(self, A):
    """
    Finds the contiguous subarray with the largest sum (Kadane's Algorithm).

        Strategy: Dynamic Programming / Greedy
        --------------------------------------
        We iterate through the array maintaining a 'cur_sum'.
        At each step 'i', we make a choice:
        1. Extend the existing subarray: (cur_sum + A[i])
        2. Start a new subarray at A[i]: (A[i])
        
        We choose the option that gives the larger value: 
        cur_sum = max(A[i], cur_sum + A[i])

        Complexity Analysis:
        --------------------
        Time Complexity: O(N) - Single pass.
        Space Complexity: O(1) - Only scalar variables used.

        Example Trace:
        --------------
        Input: [-2, 1, -3, 4, -1, 2, 1]

        1. i=0, Val=-2. 
           - cur_sum = -2. max_sum = -2.
        
        2. i=1, Val=1. 
           - Option A (Extend): -2 + 1 = -1
           - Option B (Start New): 1
           - Winner: 1. (Reset! Previous negative sum was a burden).
           - max_sum = 1.

        3. i=2, Val=-3.
           - Option A (Extend): 1 + (-3) = -2.
           - Option B (Start New): -3.
           - Winner: -2. (Extend, even though it lowered sum, it's better than -3).
           - max_sum = 1.

        4. i=3, Val=4.
           - Option A (Extend): -2 + 4 = 2.
           - Option B (Start New): 4.
           - Winner: 4. (Reset! Previous sum -2 was a burden).
           - max_sum = 4.

        5. i=4 to 6 (Vals -1, 2, 1):
           - We keep extending as the sum stays positive.
           - Final chunk [4, -1, 2, 1] sums to 6.
           - max_sum = 6.
    """

    if not A:
      return 0
    
    max_sum = A[0]
    cur_sum = A[0]
    for i in range(1, len(A)):
      cur_sum = max(A[i], cur_sum + A[i])
      max_sum = max(max_sum, cur_sum)

    return max_sum