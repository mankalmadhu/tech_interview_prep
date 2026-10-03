"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/bit_manipulation/number_of_one_bits.py until you're done.

Problem (Number of 1 Bits, LeetCode 191 / Hamming Weight):

Write a function that takes an unsigned integer and returns the
number of '1' bits it has (also known as the Hamming weight).

Example:
  n = 11 (binary: 1011)
  output = 3

Write your solution below.
"""


def hamming_weight(n):
    count = 0
    while n != 0:
        if (n & 1):
            count += 1
        n >>=1

    return count



if __name__ == "__main__":
    print(hamming_weight(11))  # expect 3 (1011)
    print(hamming_weight(0))  # expect 0
    print(hamming_weight(128))  # expect 1 (10000000)

    assert hamming_weight(11) == 3
    assert hamming_weight(0) == 0
    assert hamming_weight(128) == 1
    assert hamming_weight(255) == 8
    assert hamming_weight(1) == 1
    print("fixed cases passed")

    import random

    for _ in range(300):
        n = random.randint(0, 2**32 - 1)
        got = hamming_weight(n)
        want = bin(n).count("1")
        assert got == want, f"n={n}: expected {want}, got {got}"
    print("300 randomized trials passed")
