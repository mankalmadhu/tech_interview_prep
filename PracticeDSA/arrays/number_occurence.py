class Solution:
    # @param A : list of integers
    # @return a list of integers
    def findOccurences(self, A):
        """
        Counts occurrences of each distinct number via a hashmap.

        Note: The A.sort() below isn't actually required for correctness
        (counting doesn't need order) - it just adds unnecessary O(N log N)
        overhead on top of the O(N) counting pass. Kept as-is since it
        doesn't affect correctness.

        Time Complexity: O(N log N) as written (dominated by the sort;
           would be O(N) if the sort were removed).
        Space Complexity: O(N) for the hashmap of distinct values.
        """
        A.sort()
        result_dict = {}
        for num in A:
            if num in result_dict:
                result_dict[num] += 1
            else:
                result_dict[num] = 1
        return result_dict.values()


if __name__ == "__main__":
    import collections
    import random

    sol = Solution()
    inputs = [[3, 1, 3, 2, 1, 1], [], [5], [1, 1, 1]]
    expected_outputs = [
        sorted([3, 2, 1]),
        [],
        [1],
        [3],
    ]

    for idx, A in enumerate(inputs):
        result = sorted(sol.findOccurences(A[:]))
        assert result == expected_outputs[idx], (
            f"A={A}: expected {expected_outputs[idx]}, got {result}"
        )
        print(f"Expected Result: {expected_outputs[idx]}. Actual Result: {result}")
    print("All example tests passed!")

    for trial in range(200):
        n = random.randint(0, 20)
        A = [random.randint(0, 10) for _ in range(n)]
        got = sorted(Solution().findOccurences(A[:]))
        expected = sorted(collections.Counter(A).values())
        assert got == expected, f"Mismatch on {A}: got {got}, expected {expected}"

    print("All stress tests passed!")
