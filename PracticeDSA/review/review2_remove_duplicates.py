"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/two_pointer/remove_duplicates.py until you're done.

Problem: Given a SORTED array A (in-place), remove duplicates such
that each unique element appears only once, and return the new
length. Elements beyond the returned length don't matter (but the
original file sets them to -1 for clarity/testing).

Write your solution below.
"""


class Solution:
    def removeDuplicates(self, A):
        if not A:
            return 0
        slow, fast = 0,1
        while fast < len(A):
            if A[slow] != A[fast]:
                slow += 1
                A[slow] = A[fast]
            fast += 1
        return slow+1


if __name__ == "__main__":
    sol = Solution()
    # add your own test calls here once implemented
