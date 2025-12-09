#https://www.interviewbit.com/problems/rearrange-array/
class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, A):
        """
        Rearranges the array such that A[i] becomes A[A[i]] in O(1) space.

        Strategy: Encoding Two Numbers in One
        -------------------------------------
        Since all elements are in the range [0, n-1], we can store two values 
        at each index by treating the number as a base-n integer:
        
        Formula: Encoded_Val = Old_Val + (New_Val * n)

        1. Encoding Phase (Write):
           - Iterate through the array.
           - We want to store the value currently at A[A[i]] (which is our 'New_Val') 
             into position i.
           - CAUTION: The value at A[A[i]] might have already been encoded!
           - RETRIEVAL: Use `A[A[i]] % n` to always retrieve the ORIGINAL (Old) 
             value stored at that index.
           - UPDATE: A[i] = A[i] + (A[A[i]] % n) * n

        2. Decoding Phase (Read):
           - Iterate again to finalize the array.
           - A[i] = A[i] // n  (This isolates the 'New_Val' part).

        Complexity Analysis:
        --------------------
        Time Complexity: O(N)
           - Two passes over the array (one to encode, one to decode).
        Space Complexity: O(1)
           - We modify the array in-place without extra data structures.

        Example Trace:
        --------------
        Input: A = [1, 0], n = 2
        
        Phase 1: Encoding
        - i = 0: 
          - Old_Val = A[0] = 1
          - Target Index = A[0] = 1. 
          - New_Val = A[1] % 2 = 0.
          - A[0] = 1 + (0 * 2) = 1.  (Array is now [1, 0])
        
        - i = 1:
          - Old_Val = A[1] = 0
          - Target Index = A[1] = 0.
          - New_Val = A[0] % 2 = 1. (Crucial: We use % 2 to get the original 1)
          - A[1] = 0 + (1 * 2) = 2.  (Array is now [1, 2])

        Phase 2: Decoding
        - A[0] = 1 // 2 = 0
        - A[1] = 2 // 2 = 1
        
        Result: [0, 1]
        """
        n = len(A)
        for i in range(n):
            A[i] = A[i] + (A[A[i]] % n) * n
        for i in range(n):
            A[i] = A[i] // n
