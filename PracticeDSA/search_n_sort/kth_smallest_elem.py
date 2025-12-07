#https://www.interviewbit.com/problems/kth-smallest-element-in-the-array/
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        low = min(A)
        high = max(A)
        while low < high:
            mid = (low+high)//2
            count = 0
            for num in A:
                if num <= mid:
                    count += 1
            if count < B:
                low = mid+1
            else:
                high = mid
        
        return low
