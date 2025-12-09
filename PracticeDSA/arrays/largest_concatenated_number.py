class Solution:
  # @param A : tuple of integers
  # @return a strings
  # https://www.interviewbit.com/problems/largest-number/
  def largestNumber(self, A):
    """
    Arranges a list of non-negative integers to form the largest number.

        Strategy: Sorting with Custom Comparator
        ----------------------------------------
        1. Problem: Standard lexicographical sort fails (e.g., "30" > "3" is True, 
           but "330" > "303", so 3 should come before 30).
        2. Solution: To decide if X comes before Y, we compare the concatenated 
           combinations: (X + Y) vs (Y + X).
           - If (str(X) + str(Y)) > (str(Y) + str(X)), then X comes first.
           - If (str(X) + str(Y)) < (str(Y) + str(X)), then Y comes first.
        3. Edge Case: If the result starts with '0' (e.g., input was [0, 0]), 
           return "0".

        Complexity Analysis:
        --------------------
        Time Complexity: O(N * log N * K)
           - N is the number of elements. K is the max length of a number.
           - Sorting takes O(N log N) comparisons. Each comparison takes O(K) 
             for string concatenation.
        Space Complexity: O(N)
           - To store the string representations.

        Example Trace:
        --------------
        Input: [3, 30, 34]
        
        1. Compare 3 and 30:
           - "3" + "30" = "330"
           - "30" + "3" = "303"
           - "330" > "303" -> [3, 30] (3 comes before 30)

        2. Compare 30 and 34:
           - "30" + "34" = "3034"
           - "34" + "30" = "3430"
           - "3430" > "3034" -> [34, 30] (34 comes before 30)

        3. Compare 3 and 34:
           - "3" + "34" = "334"
           - "34" + "3" = "343"
           - "343" > "334" -> [34, 3] (34 comes before 3)

        Sorted Result: [34, 3, 30] -> Concatenated: "34330"
    """

    from functools import cmp_to_key

    def compare_adjacent(a, b):
      ab = str(a) + str(b)
      ba = str(b) + str(a)
      if ab > ba:
        return -1
      elif ab < ba:
        return 1
      else:
        return 0

    A_sorted = sorted(A, key=cmp_to_key(compare_adjacent))

    return "".join(map(str, A_sorted)) if A_sorted[0] != 0 else "0"


def main():
  inputs = [[3, 30, 34, 5, 9], [
      0,
      0,
      0,
      0,
  ]]
  expected_outputs = ["9534330", "0"]
  for idx, A in enumerate(inputs):
    sol = Solution()
    result = sol.largestNumber(A)
    print(f"Expected Result: {expected_outputs[idx]}.Actual Result:{result}")
