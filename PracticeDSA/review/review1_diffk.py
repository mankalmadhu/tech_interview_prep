"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/two_pointer/diffk.py until you're done.

Problem: Given a sorted array A of integers and an integer B,
determine if there exists a pair of indices i != j such that
A[i] - A[j] == B (i.e. an "arbitrary pair with a given absolute
difference" style problem — but check exact original for +/- B).

Write your solution below.
"""


class Solution:
    def diffPossible(self, A, B):
        i, j = 0,1

        if len(A) < 2:
            return 0
        while i < len(A) and j < len(A):
            if i != j and A[j] - A[i] == B:
                return 1
            if A[j] - A[i] < B:
                j += 1
            else:
                i += 1

        return 0


if __name__ == "__main__":
    sol = Solution()
    # add your own test calls here once implemented
