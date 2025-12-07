#https://www.interviewbit.com/problems/greatest-common-divisor/
class Solution:
    def gcd(self, A, B):
        while B:
            A, B = B, A % B
        return A