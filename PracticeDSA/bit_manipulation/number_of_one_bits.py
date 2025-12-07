#https://www.interviewbit.com/problems/number-of-1-bits/
class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        A_bin = bin(A)[2:]
        one_count = 0
        for i in A_bin:
            if i=='1':
                one_count += 1
        return one_count
