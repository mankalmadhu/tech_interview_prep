class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        """
        Calculates the minimum number of parentheses needed to make the string valid.

        Strategy: Stack + Counter
        -------------------------
        1. We use a Stack to track unmatched OPENING parentheses '('.
        2. We use a Counter to track unmatched CLOSING parentheses ')'.
        
        Logic:
        - Iterate through the string.
        - Case '(': Always push to stack. It waits for a matching ')'.
        - Case ')':
          - If Stack is not empty: We found a match! Pop from stack.
          - If Stack is empty: This ')' has no matching opener. Increment Counter.
        
        Final Result:
        - The counter holds the number of ')' that need an opener added.
        - The stack length holds the number of '(' that need a closer added.
        - Result = Counter + len(Stack).

        Complexity:
        -----------
        Time: O(N) - Single pass.
        Space: O(N) - Stack size in worst case (e.g. "(((((").
        """
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
