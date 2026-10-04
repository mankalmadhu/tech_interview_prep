"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/math/palindrome_integer.py until you're done.

Problem (Palindrome Integer):

Given an integer A, determine if it reads the same forwards and
backwards. Return 1 if palindrome, 0 otherwise. Negative numbers
are never palindromes (because of the leading '-').

Example:
  A = 121 -> output = 1
  A = -121 -> output = 0
  A = 123 -> output = 0

Write your solution below.
"""


def is_palindrome(A):
    if A<0:
        return 0

    return 1 if  (A == rev_nums(A)) else 0

def rev_nums(A):
    A_rev = 0

    while A > 0:
        digit =  A%10
        A_rev = (A_rev * 10)+ digit
        A = A // 10
    return A_rev


if __name__ == "__main__":
    print(is_palindrome(121))  # expect 1
    print(is_palindrome(-121))  # expect 0
    print(is_palindrome(123))  # expect 0
    print(is_palindrome(7))  # expect 1

    import random

    for trial in range(300):
        A = random.randint(-100000, 100000)
        got = is_palindrome(A)
        expected = 1 if (A >= 0 and str(A) == str(A)[::-1]) else 0
        assert got == expected, f"Mismatch on {A}: got {got}, expected {expected}"

    print("All stress tests passed!")
