class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        count = 0
        for i in range(len(A)):
            if A[i] in vowels:
                count += len(A) - i
        return count % 10003


if __name__ == "__main__":
    sol = Solution()
    inputs = ["ABEC", "", "bcd", "a", "aeiou"]
    expected_outputs = [6, 0, 0, 1, 15]
    for idx, A in enumerate(inputs):
        result = sol.solve(A)
        assert result == expected_outputs[idx], (
            f"A={A!r}: expected {expected_outputs[idx]}, got {result}"
        )
        print(f"Expected Result: {expected_outputs[idx]}.Actual Result:{result}")
    print("All tests passed!")
