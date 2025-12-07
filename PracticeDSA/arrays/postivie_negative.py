#https://www.interviewbit.com/problems/positive-negative/
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        postive_num_count = 0
        negative_num_count = 0
        
        for i in A:
            if i >0:
                postive_num_count +=1
            elif i <0:
                negative_num_count +=1
        
        return [postive_num_count,negative_num_count ]
                
