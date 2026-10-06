class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        """
        Time Complexity: O(N log N) - dominated by the sort.
        Space Complexity: O(1) auxiliary (ignoring sort's internal space).
        """
        if not A:
            return 0
        A.sort()
        return A[-1] + A[0]


class SolutionOptimal:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        """
        Single-pass approach: track running min/max instead of sorting.

        Time Complexity: O(N) - one pass over the array.
        Space Complexity: O(1).
        """
        if not A:
            return 0

        min_num = float("inf")
        max_num = float("-inf")

        for num in A:
            if num < min_num:
                min_num = num
            if num > max_num:
                max_num = num

        return min_num + max_num


if __name__ == "__main__":
    inputs = [[3, 2, 1, 4], [], [5], [-3, -1, -7, -2]]
    expected_outputs = [5, 0, 10, -8]

    for idx, A in enumerate(inputs):
        result = Solution().solve(A[:])
        result_optimal = SolutionOptimal().solve(A[:])
        assert result == expected_outputs[idx], (
            f"A={A}: expected {expected_outputs[idx]}, got {result}"
        )
        assert result_optimal == expected_outputs[idx], (
            f"A={A}: expected {expected_outputs[idx]}, got {result_optimal}"
        )
        print(f"Expected Result: {expected_outputs[idx]}. Actual Result: {result}")
    print("All example tests passed!")

    import random

    for trial in range(300):
        n = random.randint(0, 20)
        A = [random.randint(-100, 100) for _ in range(n)]
        got = Solution().solve(A[:])
        got_optimal = SolutionOptimal().solve(A[:])
        expected = 0 if not A else max(A) + min(A)
        assert got == expected, f"Mismatch (Solution) on {A}: got {got}, expected {expected}"
        assert got_optimal == expected, (
            f"Mismatch (SolutionOptimal) on {A}: got {got_optimal}, expected {expected}"
        )

    print("All stress tests passed!")
