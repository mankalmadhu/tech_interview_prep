"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/strings/palindrome.py until you're done.

Problem: Given a string A, determine if it is a palindrome,
considering only alphanumeric characters and ignoring case.
Return 1 if it is a palindrome, else 0.

Write your solution below.
"""


class Solution:
    def isPalindrome(self, A):
        high = len(A) - 1
        low = 0
        while low < high:
            if not A[low].isalnum():
                low+=1
                continue
            if not A[high].isalnum():
                high-=1
                continue
            if A[low].lower() != A[high].lower():
                return 0

            low +=1
            high -=1

        return 1





if __name__ == "__main__":
    sol = Solution()
    # add your own test calls here once implemented
