"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/two_pointer/merge_sorted_lists.py until you're done.

Problem (InterviewBit "Merge Two Sorted Lists II"): Given two
sorted integer arrays A and B (of possibly different sizes, no
extra padding in A), merge B into A in-place so that A becomes a
single sorted list containing all elements from both A and B.
No return value needed — mutate A directly.

Write your solution below.
"""


class Solution:
    def merge(self, A, B):
        i,j = 0,0

        while i < len(A) or j < len(B):
            if i >= len(A):
                A.append(B[j])
                j += 1
            if j < len(B) and A[i] > B[j]:
                A.insert(i, B[j])
                j += 1
            i += 1

    def merge1(self, A, B):

        m = len(A)
        n = len(B)

        i = m-1
        j = n-1
        k = m+n-1

        A.extend([0]*n)

        while i >=0 and j>=0:
            if A[i] > B[j]:
                A[k] = A[i]
                i -= 1
            else:
                A[k] = B[j]
                j -= 1

            k -= 1

        while j >=0:
            A[k] = B[j]
            j -= 1
            k -= 1


if __name__ == "__main__":
    sol = Solution()
    # add your own test calls here once implemented
