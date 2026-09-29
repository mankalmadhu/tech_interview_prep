"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/two_pointer/triplet_sum.py until you're done (it's
currently broken/unparseable anyway).

Problem: Given an array A of integers and a target integer B,
find the sum of three integers in A such that the sum is closest
to B. Return that sum (not the triplet itself).

Write your solution below.
"""


class Solution:
    def threeSumClosest(self, A, B):
        A.sort()
        closest_sum = float('inf')
        for i in range( len(A)-2):
            left, right = i+1, len(A)-1
            while left < right:
                cur_sum  = A[i] + A[left] + A[right]
                if abs(cur_sum - B) < abs(closest_sum - B):
                    closest_sum = cur_sum
                if cur_sum < B:
                    left += 1
                else:
                    right -= 1
        return closest_sum



if __name__ == "__main__":
    sol = Solution()
    # add your own test calls here once implemented
