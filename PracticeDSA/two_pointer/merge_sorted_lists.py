# https://www.interviewbit.com/problems/merge-two-sorted-lists-ii/
class Solution:
  # @param A : list of integers
  # @param B : list of integers
    def merge(self, A, B):
            i=j=0
            while i<len(A) or j<len(B):
                if i >= len(A):
                    A.append(B[j])
                    j += 1
                if j < len(B) and A[i] > B[j]:
                    A.insert(i, B[j])
                    j += 1
                i +=1