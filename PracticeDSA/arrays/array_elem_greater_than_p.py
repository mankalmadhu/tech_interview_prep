class Solution:
  # @param A : list of integers
  # @return an integer
  # https://www.interviewbit.com/problems/noble-integer/
  def solve(self, A):
    """
       this problem is essentialy for a value in any given index, 
       if the array has same count of remianing elements in the array from current index,
        than we have found a noble integer (repeating values are skipped)
        The Logic:
        The logic relies entirely on the array being sorted in ascending order.

        - A[i]: This is your candidate for P.
        - n: Total elements in the array.
        - i: Current position (0-indexed).

        In a sorted array, if you are at index i, then all elements after index i 
        are guaranteed to be greater than or equal to A[i].

        The number of elements after index i is exactly (Total Elements - Elements up to i).
        Count = n - (i + 1), which simplifies to n - 1 - i.

        So the condition `A[i] == n - 1 - i` essentially asks:
        "Is the value at this position equal to the count of elements remaining to its right?"

        Visual Example:
        Let's trace A = [1, 2, 3, 3] (Sorted). Here, n = 4.

        | Index (i) | Value (A[i]) | Formula (n-1-i) | Meaning (Elements to the right) | Match? |
        | :--- | :--- | :--- | :--- | :--- |
        | 0 | 1 | 4 - 1 - 0 = 3 | There are 3 numbers to the right: [2, 3, 3] | 1 != 3 (No) |
        | 1 | 2 | 4 - 1 - 1 = 2 | There are 2 numbers to the right: [3, 3] | 2 == 2 (Yes!) |
        | 2 | 3 | 4 - 1 - 2 = 1 | There is 1 number to the right: [3] | 3 != 1 (No) |

        The algorithm finds 2 is the noble integer because its value (2) equals 
        the count of numbers strictly greater than it (which are the two 3s to its right).

        Note on Duplicates: 
        This logic assumes strict inequality. That is why the code has the check 
        `if A[i] == A[i+1]: continue`. This ensures we only compare the *last* instance of a number against the count of numbers *strictly* greater than it.
        """

    A.sort()
    count = 0
    n = len(A)
    for i in range(n):
      if i < n - 1 and A[i] == A[i + 1]:
        continue
      if A[i] == n-1-i:
        count += 1
    return count if count > 0 else -1

if __name__ == "__main__":
  sol = Solution()
  inputs = [[3, 2, 1, 3],[1, 1, 3, 3]]
  expected_outputs = [1, -1]

  for idx, A in enumerate(inputs):
    result = sol.solve(A)
    print(f"Expected Result: {expected_outputs[idx]}.Actual Result:{result}")

