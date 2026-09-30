"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/bit_manipulation/single_number.py until you're done.

Problem (Single Number, LeetCode 136 / InterviewBit):
https://www.interviewbit.com/problems/single-number/

Given a non-empty array of integers A, every element appears twice
except for one element which appears only once. Find that single
element.

Constraint: your solution should have O(N) time and O(1) space (no
hash set/counting allowed).

Example:
  A = [4, 1, 2, 1, 2] -> 4
  A = [1]             -> 1

Write your solution below.
"""


class Solution:
    def singleNumber(self, A):
        result = 0
        for i in A:
            result ^= i

        return result


if __name__ == "__main__":
    # add your own test calls here once implemented
    pass
