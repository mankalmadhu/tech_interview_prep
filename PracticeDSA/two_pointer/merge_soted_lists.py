class Solution:
    # @param A : list of integers
    # @param B : list of integers
    def merge(self, A, B):
        m = len(A)
        n = len(B)
        i = m - 1
        j = n - 1
        k = m + n - 1

        # Extend A to accommodate all elements from B
        A.extend([0] * n)

        # Merge from the end, handling negative numbers properly
        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                A[k] = A[i]
                i -= 1
            else:
                A[k] = B[j]
                j -= 1
            k -= 1

        # Copy remaining elements from B (if any)
        while j >= 0:
            A[k] = B[j]
            j -= 1
            k -= 1


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
