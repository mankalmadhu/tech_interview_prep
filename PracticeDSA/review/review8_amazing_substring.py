"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/strings/amazing_substring.py until you're done.

Problem: "Amazing Substrings" — given a string A, count the
number of substrings that START with a vowel (a, e, i, o, u,
case-insensitive). Since the count can be large, return it
modulo 10003.

Example: A = "ABEC" -> 6
  (vowel-starting chars: 'A' at idx 0, 'E' at idx 2)

Write your solution below.
"""


class Solution:
    def solve(self, A):
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        count = 0
        for i in range(len(A)):
            if A[i] in vowels:
                count += len(A) - i
        return count % 10003



if __name__ == "__main__":
    sol = Solution()
    # add your own test calls here once implemented
