"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/arrays/even_product.py until you're done.

Problem (Even Product, InterviewBit):

https://www.interviewbit.com/problems/even-product/

Given an array A of n integers whose product is currently ODD
(meaning every element is odd), count the number of distinct
non-empty subsets of indices you could choose such that changing
those chosen indices' values to even numbers would make the
overall product even. Return the count modulo 1000000007.

Example:
  A = [1, 3, 5]  (n=3)
  output = 2^3 - 1 = 7  (any non-empty subset works)

Write your solution below.
"""


def even_product_count(A):
    """
    For each of the n elements, there are 2 independent choices: include it
    in the chosen subset, or don't. These choices are independent, so total
    subsets = 2 * 2 * ... * 2 (n times) = 2**n (the power set).

    Of these 2**n subsets, only the EMPTY subset fails to make the product
    even (since changing a non-empty subset's values to even numbers always
    introduces at least one even factor). So valid count = 2**n - 1.

    NOTE on complexity: (2**n) % MOD computes the full un-reduced 2**n first
    (a number with ~n*log10(2) digits) before reducing - this does more work
    as n grows than necessary. Using pow(2, n, MOD) (3-arg modular
    exponentiation) keeps every intermediate value bounded by MOD, giving a
    true O(log n) time, O(1) space solution regardless of how large n gets.
    """
    n = len(A)
    return ((2**n) - 1) % 1000000007


if __name__ == "__main__":
    print(even_product_count([1, 3, 5]))  # expect 7
    print(even_product_count([1]))  # expect 1
    print(even_product_count([1, 1, 1, 1]))  # expect 15

    import random

    MOD = 1000000007
    for trial in range(300):
        n = random.randint(1, 1000)
        arr = [1] * n  # product is odd regardless of exact values
        got = even_product_count(arr)
        expected = (pow(2, n, MOD) - 1) % MOD
        assert got == expected, f"Mismatch on n={n}: got {got}, expected {expected}"

    print("All stress tests passed!")
