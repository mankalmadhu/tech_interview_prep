class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        n = len(A)
        if n == 0:
            return None
        if n == 1:
            return A[0]
        count = 0
        candidate = None
        for num in A:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate


def brute_force_majority(A):
    from collections import Counter
    counts = Counter(A)
    n = len(A)
    for val, c in counts.items():
        if c > n // 2:
            return val
    return None


def main():
    inputs = [[3, 2, 3], [2, 1, 2], [1, 2, 2, 2, 3, 5]]
    expected_outputs = [3, 2, 1]
    for idx, A in enumerate(inputs):
        sol = Solution()
        result = sol.majorityElement(A)
        print(f"Expected Result: {expected_outputs[idx]}.Actual Result:{result}")

    import random

    for trial in range(300):
        n = random.randint(1, 50)
        majority_val = random.randint(-5, 5)
        half = n // 2 + 1
        arr = [majority_val] * half
        arr += [random.randint(-5, 5) for _ in range(n - half)]
        random.shuffle(arr)

        sol = Solution()
        got = sol.majorityElement(arr)
        expected = brute_force_majority(arr)
        assert got == expected, f"Mismatch on {arr}: got {got}, expected {expected}"

    print("All stress tests passed!")


if __name__ == "__main__":
    main()
