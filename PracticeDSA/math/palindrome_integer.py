class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        A_str = str(A)
        A_str_rev = A_str[::-1]
        return 1 if (A_str == A_str_rev) else 0

    def isPalindromeNumeric(self, A):
        """Reverses A via repeated div/mod instead of string reversal."""
        if A < 0:
            return 0

        rev = 0
        n = A
        while n > 0:
            digit = n % 10
            rev = rev * 10 + digit
            n //= 10

        return 1 if A == rev else 0


if __name__ == "__main__":
    sol = Solution()
    for method in (sol.isPalindrome, sol.isPalindromeNumeric):
        print(method(121))  # expect 1
        print(method(-121))  # expect 0
        print(method(123))  # expect 0
        print(method(7))  # expect 1

    import random

    for trial in range(300):
        A = random.randint(-100000, 100000)
        expected = 1 if (A >= 0 and str(A) == str(A)[::-1]) else 0
        for method in (sol.isPalindrome, sol.isPalindromeNumeric):
            got = method(A)
            assert got == expected, f"{method.__name__} mismatch on {A}: got {got}, expected {expected}"

    print("All stress tests passed!")
