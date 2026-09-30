# https://www.interviewbit.com/problems/greatest-common-divisor/
class Solution:
    def gcd(self, A, B):
        """
        Algorithm: Euclidean Algorithm
        - Time Complexity: O(log(min(A, B))). The modulo operation more than halves
          the maximum of the two numbers in every two steps, leading to logarithmic decay.
        - Space Complexity: O(1) auxiliary space as it is implemented iteratively.
        """
        while B:
            A, B = B, A % B
        return A


if __name__ == "__main__":
    import math
    import random

    sol = Solution()
    fixed_cases = [(12, 18, 6), (7, 13, 1), (0, 5, 5), (5, 0, 5), (17, 17, 17)]
    for A, B, expected in fixed_cases:
        got = sol.gcd(A, B)
        assert got == expected, f"gcd({A}, {B}) = {got}, expected {expected}"
    print(f"All {len(fixed_cases)} fixed cases passed.")

    random.seed(21)
    for _ in range(2000):
        A = random.randint(0, 10000)
        B = random.randint(0, 10000)
        expected = math.gcd(A, B)
        got = sol.gcd(A, B)
        assert got == expected, f"gcd({A}, {B}) = {got}, expected {expected}"
    print("2000 randomized stress trials passed.")
