"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/search_n_sort/max_blade_height.py until you're done.

Problem (EKO / Woodcutting, InterviewBit):
https://www.interviewbit.com/problems/woodcutting-made-easy/

Given an array A of tree heights and an integer B (units of wood needed),
a woodcutting machine is set to some blade height H. For each tree taller
than H, the machine collects (tree_height - H) units of wood; shorter
trees are untouched.

Find the MAXIMUM integer blade height H such that the total wood
collected across all trees is >= B.

Example:
  A = [20, 15, 10, 17], B = 7  -> answer: 15
  A = [4, 42, 40, 26, 46], B = 20 -> answer: 36

Write your solution below.
"""


class Solution:
    def solve(self, A, B):
        high = max(A)
        low = 0
        max_blade_height = 0

        while low < high:
            mid = (low+high)//2
            wood_collected = 0

            for i in range(len(A)):
                if A[i] > mid:
                    wood_collected += A[i] -mid

            if wood_collected >= B:
                low = mid +1
                max_blade_height = mid
            else:
                high  = mid

        return max_blade_height


if __name__ == "__main__":
    # add your own test calls here once implemented
    s = Solution()
    A = [20, 15, 10, 17]
    B = 7
    print(s.solve(A, B))
    A = [4, 42, 40, 26, 46]
    B = 20
    print(s.solve(A, B))
