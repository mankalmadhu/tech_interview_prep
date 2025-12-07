"""
The core of the algorithm is based on that principle: if a positive integer k is in its correct place, it should be at index k-1. 🧠

The expression A[i] != A[A[i] - 1] is a clever and crucial part of the algorithm's logic. Let's break down why it's used for the swap condition:
A[i] is the number we are currently considering.
A[i] - 1 is the correct index where A[i] should be located.
A[A[i] - 1] is the number that is currently at the correct index.
The comparison A[i] != A[A[i] - 1] checks if the number we're holding (A[i]) is different from the number already in its correct "home" position. This prevents an infinite loop that would occur if we tried to swap a number with itself or with an identical number already in the correct spot.

Essentially, the condition ensures that we only perform a swap if the current number A[i] needs to be moved and if its correct position is not already occupied by the same value. This ensures each number is moved at most once to its final position, allowing the algorithm to maintain its O(n) time complexity.
"""

class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        n = len(A)
    
        i = 0
        while i < n:
            correct_pos = A[i] - 1
            if 1 <= A[i] <= n and A[i] != A[correct_pos]:
                A[i], A[correct_pos] = A[correct_pos], A[i]
            else:
                i += 1
    
        for i in range(n):
            if A[i] != i + 1:
                return i + 1
    
        return n + 1


def main():

    inputs = [[1, 2, 0], [3, 4, -1, 1], [1, 2, 3], [1, 2, 3, 4, 5, 6, 7],
              [-8, -7, -6]]
    expected_outputs = [3, 2, 4, 8, 1]
    for idx, A in enumerate(inputs):
        sol = Solution()
        result = sol.firstMissingPositive(A)
        print(
            f"Expected Result: {expected_outputs[idx]}.Actual Result:{result}")
