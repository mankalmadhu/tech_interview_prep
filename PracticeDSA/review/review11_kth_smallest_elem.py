"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/search_n_sort/kth_smallest_elem.py until you're done.

Problem: Given an array A and an integer B, find the B-th
smallest element in A (1-indexed, B=1 means smallest element).

Pick ONE approach to implement (your choice):
  (a) Binary search on the VALUE range [min(A), max(A)]
  (b) QuickSelect (partition-based, like quick_sort but only
      recurse into the side containing the answer)

Write your solution below.
"""


class Solution:
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
                low = mid + 1
            else:
                high = mid

        return low

    def kthsmallest1(self, A, B):
        return self.quickselect(A,B, 0, len(A)-1)

    def quickselect(self, A, B, low, high):
        if low == high:
            return A[low]

        pivot_idx =  self.partiton(A, low, high)
        rank = pivot_idx - low + 1

        if rank == B:
            return A[pivot_idx]
        elif rank < B:
            return self.quickselect(A,B-rank,pivot_idx+1, high)
        else:
            return self.quickselect(A,B,low, pivot_idx-1)



    def partiton(self,A, low,high):
        pivot = A[high]
        i = low -1
        for j in range(low,high):
            if A[j] <= pivot:
                i += 1
                A[j],A[i] = A[i], A[j]

        A[i+1], A[high] = A[high], A[i+1]
        return i+1




if __name__ == "__main__":
    sol = Solution()
    # add your own test calls here once implemented
