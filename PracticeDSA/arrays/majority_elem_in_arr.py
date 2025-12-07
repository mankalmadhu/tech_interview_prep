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
            count += (1 if num == candidate else -1)
        return candidate


def main():
    inputs = [[3, 2, 3], [2, 1, 2], [1, 2, 2, 2, 3, 5]]
    expected_outputs = [3, 2, 1]
    for idx, A in enumerate(inputs):
        sol = Solution()
        result = sol.majorityElement(A)
        print(
            f"Expected Result: {expected_outputs[idx]}.Actual Result:{result}")

if __name__ == "__main__":
    main()