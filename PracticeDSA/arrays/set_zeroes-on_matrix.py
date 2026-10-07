class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        """
        Sets entire row and column to zeroes if an element is 0, in-place.

        Strategy: O(M+N) Space (Row/Col Sets)
        -------------------------------------
        Track which rows and columns contain a 0 using two sets, then
        zero out every cell whose row or column is in those sets.

        See SolutionOptimal below for the O(1) space variant that uses
        the first row/column of the matrix itself as flag storage.

        Complexity Analysis:
        --------------------
        Time Complexity: O(M * N)
           - Two passes over the matrix.
        Space Complexity: O(M + N)
           - Two sets to track affected rows/columns.
        """
        rows = set()
        cols = set()
        m = len(A)
        n = len(A[0])
        for i in range(m):
            for j in range(n):
                if A[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    A[i][j] = 0


class SolutionOptimal:
    """
    Smart Review Discussion (2026-05-24):
    -------------------------------------
    We discussed the trade-off between the O(M+N) space solution (using sets) and this O(1) space solution.
    While the O(1) solution is technically "optimal" for memory, it requires strictly O(M*N) iterations even if there are very few zeroes.
    The O(M+N) space solution can be faster in practice because iterating through the sets of rows/cols directly avoids unnecessary operations on unaffected rows.

    However, the O(1) space constraint is a classic interview requirement. It is achieved by using the first row
    and first column as marker flags to store whether a row/column needs to be zeroed. We use two
    booleans `zero_fr` and `zero_fc` to prevent the first row and column from corrupting each other's state initially.

    Time Complexity: O(M * N)
    Space Complexity: O(1)
    """

    def setZeroes(self, A: list[list[int]]) -> list[list[int]]:
        m = len(A)
        n = len(A[0])

        zero_fr, zero_fc = False, False

        for i in range(m):
            for j in range(n):
                if A[i][j] == 0:
                    if i == 0:
                        zero_fr = True
                    if j == 0:
                        zero_fc = True
                    if i > 0 and j > 0:
                        A[i][0] = 0
                        A[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if A[i][0] == 0 or A[0][j] == 0:
                    A[i][j] = 0

        if zero_fr:
            A[0] = [0] * n

        if zero_fc:
            for i in range(m):
                A[i][0] = 0

        return A


if __name__ == "__main__":
    import random

    def make_cases():
        return [
            ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
            (
                [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
                [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
            ),
            ([[1, 2], [3, 4]], [[1, 2], [3, 4]]),
        ]

    for A, expected in make_cases():
        A_copy = [row[:] for row in A]
        Solution().setZeroes(A_copy)
        assert A_copy == expected, f"Solution: A={A}, got={A_copy}, expected={expected}"

    for A, expected in make_cases():
        A_copy = [row[:] for row in A]
        got = SolutionOptimal().setZeroes(A_copy)
        assert got == expected, (
            f"SolutionOptimal: A={A}, got={got}, expected={expected}"
        )

    def brute_force(A):
        m = len(A)
        n = len(A[0])
        rows, cols = set(), set()
        for i in range(m):
            for j in range(n):
                if A[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    A[i][j] = 0
        return A

    for _ in range(300):
        m = random.randint(1, 6)
        n = random.randint(1, 6)
        A = [[random.randint(0, 3) for _ in range(n)] for _ in range(m)]
        A1 = [row[:] for row in A]
        A2 = [row[:] for row in A]
        A3 = [row[:] for row in A]
        expected = brute_force(A1)
        Solution().setZeroes(A2)
        assert A2 == expected
        assert SolutionOptimal().setZeroes(A3) == expected

    print("All tests passed!")
