"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/math/gcd.py until you're done.

Problem (Greatest Common Divisor, InterviewBit):
https://www.interviewbit.com/problems/greatest-common-divisor/

Given two non-negative integers A and B, find their GCD.

Example:
  A=12, B=18 -> 6
  A=7,  B=13 -> 1
  A=0,  B=5  -> 5

Write your solution below (Euclidean algorithm).
"""


class Solution:
    def gcd(self, A, B):
        while A:
            B,A = A, B%A

        return B


if __name__ == "__main__":
    # add your own test calls here once implemented
    pass
