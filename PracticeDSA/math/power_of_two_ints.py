# https://www.interviewbit.com/problems/power-of-two-integers/
class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        """
        Checks if A can be expressed as x^y where x > 0 and y > 1.

        Essence of the Solution:
        - We take the log of the number for different bases.
        - If for any of the bases the log value is an integer, then we have our answer.
        - The bases to look at are upper-bounded by the square root of the number.

        Strategy: Brute Force on Base
        -----------------------------
        We iterate through possible bases 'i' starting from 2.

        Upper Bound for Base:
        - Since the exponent 'y' must be at least 2, the base 'i' cannot exceed sqrt(A).
        - If i > sqrt(A), then i^2 would be > A.
        - Range: [2, int(sqrt(A)) + 1].

        Precision Logic:
        - We calculate the exponent p = log(A, i).
        - Since log returns floats (e.g., 3.0000001), we round to 6 decimals.
        - We check if p is an integer by comparing ceil(p) == floor(p).

        Complexity Analysis:
        --------------------
        Time Complexity: O(sqrt(A))
           - The loop runs from 2 to sqrt(A). This is much faster than O(A)
             but slower than O(log A).
        Space Complexity: O(1)
           - Constant extra space.
        """
        import math

        if A == 1:
            return 1
        for i in range(2, int(math.sqrt(A)) + 1):
            p = math.log(A, i)
            p = round(p, 6)
            if math.ceil(p) == math.floor(p):
                return 1
        return 0

    def isPowerExactCheck(self, A):
        """
        Same idea, but verifies the candidate exponent with exact integer
        exponentiation instead of rounding the float log value. This avoids
        relying on a fixed decimal precision (e.g. round(p, 6) could still
        be fooled for sufficiently large A where floating-point error
        exceeds that tolerance) - the final check is always exact.

        Time Complexity: O(sqrt(A))
        Space Complexity: O(1)
        """
        import math

        if A == 1:
            return 1
        for i in range(2, int(math.sqrt(A)) + 1):
            p = math.log(A, i)
            if i ** round(p) == A:
                return 1
        return 0


if __name__ == "__main__":
    sol = Solution()
    for fn in (sol.isPower, sol.isPowerExactCheck):
        assert fn(16) == 1
        assert fn(10) == 0
        assert fn(1) == 1
        assert fn(512) == 1  # 8^3
        assert fn(2) == 0
        assert fn(4) == 1
        assert fn(2401) == 1  # 7^4
    print("fixed cases passed (both approaches)")

    def brute_force(a):
        if a == 1:
            return 1
        for x in range(2, int(a**0.5) + 2):
            y = 2
            val = x**y
            while val < a:
                y += 1
                val = x**y
            if val == a:
                return 1
        return 0

    for n in range(1, 2000):
        want = brute_force(n)
        got1 = sol.isPower(n)
        got2 = sol.isPowerExactCheck(n)
        assert got1 == want, f"isPower: n={n}, expected {want}, got {got1}"
        assert got2 == want, f"isPowerExactCheck: n={n}, expected {want}, got {got2}"
    print("exhaustive 1..2000 trials passed (both approaches)")
