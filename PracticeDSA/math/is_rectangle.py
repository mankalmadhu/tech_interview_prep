class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):

        all4equal = A == B == C == D
        acbd = A == C and B == D
        abcd = A == B and C == D
        adbc = A == D and B == C

        return 1 if (all4equal or acbd or abcd or adbc) else 0


def _brute_force_is_rectangle(A, B, C, D):
    from collections import Counter
    counts = sorted(Counter([A, B, C, D]).values(), reverse=True)
    return 1 if counts in ([4], [2, 2]) else 0


if __name__ == "__main__":
    sol = Solution()
    print(sol.solve(5, 5, 5, 5))  # expect 1
    print(sol.solve(2, 3, 2, 3))  # expect 1
    print(sol.solve(2, 3, 3, 4))  # expect 0
    print(sol.solve(2, 3, 3, 2))  # expect 1

    import random
    import itertools

    for trial in range(300):
        sides = [random.randint(1, 5) for _ in range(4)]
        for perm in itertools.permutations(sides):
            A, B, C, D = perm
            got = sol.solve(A, B, C, D)
            expected = _brute_force_is_rectangle(A, B, C, D)
            assert got == expected, f"Mismatch on {perm}: got {got}, expected {expected}"

    print("All stress tests passed!")
