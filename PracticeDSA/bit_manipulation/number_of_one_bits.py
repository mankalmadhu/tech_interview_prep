#https://www.interviewbit.com/problems/number-of-1-bits/
class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        """
        Calculates the Hamming weight (number of 1 bits) of an integer.

        Algorithm: Brian Kernighan's Algorithm
        - Time Complexity: O(K), where K is the number of set bits.
        - Space Complexity: O(1).
        
        Logic:
        - The operation `A & (A - 1)` perfectly deletes the rightmost `1` bit 
          from the binary representation of `A`.
        - By running this in a while loop until `A == 0`, the loop executes 
          exactly K times, completely avoiding checking all 32/64 bits.
        """
        count = 0
        while A != 0:
            A &= (A - 1)
            count += 1
        return count
