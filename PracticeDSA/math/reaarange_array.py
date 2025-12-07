#https://www.interviewbit.com/problems/rearrange-array/
class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, A):
        '''
        This algorithm, which rearranges an array such that A[i] becomes A[A[i]], works by encoding two numbers into a single array element. The core intuition is to use a number's remainder and quotient to store both the original value and the new value in the same position.

The formula A[i] = A[i] + (A[A[i]] % n) * n works as follows:
The original value at index i is stored as A[i] % n.
The new value that should be placed at index i is A[A[i]]. This value is scaled by n and added to the original value. The new value can be retrieved by performing integer division: (A[i] // n).
The crucial insight is that since all array elements are within the range [0, n-1], their original values can be recovered using the modulo operator (% n). By multiplying the new value by n, you ensure it doesn't interfere with the original value when added, because the new value is moved to a different "place value" (the tens, hundreds, etc.). This allows the element at A[i] to hold both the original value at A[i] and the original value at A[A[i]].
        '''
        n = len(A)
        for i in range(n):
            A[i] = A[i] + (A[A[i]] % n) * n
        for i in range(n):
            A[i] = A[i] // n
