#https://www.interviewbit.com/problems/flip/
class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        ans=[]
        arr=[]
        flag = True
        for i in range(len(A)):
            if A[i]=='0':
                arr.append(1)
                flag = False
            else:
                arr.append(-1)
        if flag:
            return ans
        cur_sum = 0
        max_sum = -900
        left = 0
        right = 0
        s = 0
        for i in range(len(A)):
            cur_sum+=arr[i]
            if cur_sum > max_sum:
                max_sum=cur_sum
                right = i
                left = s
            if cur_sum < 0:
                cur_sum = 0
                s = i+1
        ans.append(left+1)
        ans.append(right+1)        
        return ans  