class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        stack = []
        count = 0
        for i in A:
            if i == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                else:
                    count += 1
        return count + len(stack)


if __name__ == "__main__":
    sol = Solution()
    inputs = ["())", "(((", ")("]
    expected_outputs = [1, 3, 2]

    for idx, A in enumerate(inputs):
        result = sol.solve(A)
        print(
            f"Expected Result: {expected_outputs[idx]}.Actual Result:{result}")
