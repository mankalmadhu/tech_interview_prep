#https://www.interviewbit.com/problems/power-of-two-integers/
class Solution:
	# @param A : integer
	# @return an integer
	def isPower(self, A):
        import math
        if A==1:
            return 1
        for i in range(2,int(math.sqrt(A))+1):
            p=math.log(A,i)
            p=round(p,6)
            if math.ceil(p)==math.floor(p):
                return 1
        return 0
