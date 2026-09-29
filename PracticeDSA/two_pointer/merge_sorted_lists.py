# https://www.interviewbit.com/problems/merge-two-sorted-lists-ii/
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    def merge(self, A, B):
        """
        Merges B into A in-place, keeping A sorted.

        NOTE: uses list.insert(), which is O(N) per call (shifts all
        elements after the insertion point). Worst case (every B
        element must be inserted near the front of a large A) this
        degrades to O(N*M) / O(N^2), not O(N). See merge_soted_lists.py
        for an O(N+M) back-to-front approach without insert().
        """
        i = j = 0
        while i < len(A) or j < len(B):
            if i >= len(A):
                A.append(B[j])
                j += 1
            if j < len(B) and A[i] > B[j]:
                A.insert(i, B[j])
                j += 1
            i += 1


if __name__ == "__main__":
    import random

    sol = Solution()
    cases = [
        ([1, 5, 8], [6, 9], [1, 5, 6, 8, 9]),
        ([], [1, 2], [1, 2]),
        ([1, 2], [], [1, 2]),
        ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
        ([], [], []),
    ]
    for A, B, expected in cases:
        A2 = list(A)
        sol.merge(A2, list(B))
        assert A2 == expected, f"A={A}, B={B}: expected {expected}, got {A2}"
        print(f"A={A}, B={B} -> merged {A2}")

    random.seed(42)
    for _ in range(2000):
        n, m = random.randint(0, 8), random.randint(0, 8)
        A = sorted(random.randint(-5, 5) for _ in range(n))
        B = sorted(random.randint(-5, 5) for _ in range(m))
        expected = sorted(A + B)
        A2 = list(A)
        sol.merge(A2, list(B))
        assert A2 == expected, f"A={A}, B={B}: expected {expected}, got {A2}"

    print("All tests passed!")
