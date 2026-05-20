#https://www.interviewbit.com/problems/greatest-common-divisor/
class Solution:
    def gcd(self, A, B):
        """
        Algorithm: Euclidean Algorithm
        - Time Complexity: O(log(min(A, B))). The modulo operation more than halves 
          the maximum of the two numbers in every two steps, leading to logarithmic decay.
        - Space Complexity: O(1) auxiliary space as it is implemented iteratively.
        """
        while B:
            A, B = B, A % B
        return A