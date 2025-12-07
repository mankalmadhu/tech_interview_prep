#https://www.interviewbit.com/problems/even-product/
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n=len(A)
        return ((2**n)-1)%1000000007
