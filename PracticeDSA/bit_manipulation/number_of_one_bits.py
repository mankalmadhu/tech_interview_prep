# https://www.interviewbit.com/problems/number-of-1-bits/
class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        """
        Calculates the Hamming weight (number of 1 bits) of an integer.

        Algorithm: Brian Kernighan's Algorithm
        - Time Complexity: O(K), where K is the number of set bits.
        - Space Complexity: O(1).

        Logic:
        - The operation `A & (A - 1)` perfectly deletes the rightmost `1` bit
          from the binary representation of `A`.
        - By running this in a while loop until `A == 0`, the loop executes
          exactly K times, completely avoiding checking all 32/64 bits.
        """
        count = 0
        while A != 0:
            A &= A - 1
            count += 1
        return count

    def numSetBitsShift(self, A):
        """
        Simpler mask-and-shift approach.

        Time Complexity: O(log A) - one iteration per bit position of A,
        regardless of whether that bit is set (worse than Kernighan's O(K)
        when A is sparse, e.g. a single high bit set in a large number).
        Space Complexity: O(1).
        """
        count = 0
        while A != 0:
            if A & 1:
                count += 1
            A >>= 1
        return count


if __name__ == "__main__":
    import random

    sol = Solution()
    fixed_cases = [(11, 3), (0, 0), (128, 1), (255, 8), (1, 1)]
    for n, expected in fixed_cases:
        assert sol.numSetBits(n) == expected
        assert sol.numSetBitsShift(n) == expected
    print("fixed cases passed")

    for _ in range(300):
        n = random.randint(0, 2**32 - 1)
        want = bin(n).count("1")
        assert sol.numSetBits(n) == want, f"numSetBits: n={n}, expected {want}"
        assert sol.numSetBitsShift(n) == want, f"numSetBitsShift: n={n}, expected {want}"
    print("300 randomized trials passed (both approaches)")
