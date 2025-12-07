class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        A_str = str(A)
        A_str_rev = A_str[::-1]
        return 1 if (A_str == A_str_rev) else 0
