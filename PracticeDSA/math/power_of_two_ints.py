#https://www.interviewbit.com/problems/power-of-two-integers/
class Solution:
	# @param A : integer
	# @return an integer
	def isPower(self, A):
        """
        Checks if A can be expressed as x^y where x > 0 and y > 1.

        Strategy: Brute Force on Base
        -----------------------------
        We iterate through possible bases 'i' starting from 2.
        
        Upper Bound for Base:
        - Since the exponent 'y' must be at least 2, the base 'i' cannot exceed sqrt(A).
        - If i > sqrt(A), then i^2 would be > A.
        - Range: [2, int(sqrt(A)) + 1].

        Precision Logic:
        - We calculate the exponent p = log(A, i).
        - Since log returns floats (e.g., 3.0000001), we round to 6 decimals.
        - We check if p is an integer by comparing ceil(p) == floor(p).

        Complexity Analysis:
        --------------------
        Time Complexity: O(sqrt(A))
           - The loop runs from 2 to sqrt(A). This is much faster than O(A) 
             but slower than O(log A).
        Space Complexity: O(1)
           - Constant extra space.
        """
        import math
        if A==1:
            return 1
        for i in range(2,int(math.sqrt(A))+1):
            p=math.log(A,i)
            p=round(p,6)
            if math.ceil(p)==math.floor(p):
                return 1
        return 0
