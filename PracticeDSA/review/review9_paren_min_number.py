"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/strings/paren_min_number.py until you're done.

Problem: Given a string A consisting only of '(' and ')',
find the minimum number of parentheses that must be added to
make it valid (balanced).

Write your solution below.
"""


class Solution:
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
    # add your own test calls here once implemented
