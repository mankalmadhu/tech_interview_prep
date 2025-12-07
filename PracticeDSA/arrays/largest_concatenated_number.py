class Solution:
  # @param A : tuple of integers
  # @return a strings
  # https://www.interviewbit.com/problems/largest-number/
  def largestNumber(self, A):
    """
    The key to understanding the correct approach is to stop thinking about a fixed set of sorting rules and instead focus on a single, powerful pairwise comparison.

    For the numbers 3, 30, and 34, the sorting algorithm will perform a series of comparisons based on their concatenated forms:
    Compare 3 and 30:
    str(3) + str(30) = "330"
    str(30) + str(3) = "303"
    "330" is lexicographically greater than "303".
    Conclusion: 3 should come before 30.
    Compare 3 and 34:
    str(3) + str(34) = "334"
    str(34) + str(3) = "343"
    "343" is lexicographically greater than "334".
    Conclusion: 34 should come before 3.
    Compare 30 and 34:
    str(30) + str(34) = "3034"
    str(34) + str(30) = "3430"
    "3430" is lexicographically greater than "3034".
    Conclusion: 34 should come before 30.
    This series of comparisons establishes a clear and consistent transitive order. The number 34 must be placed before both 3 and 30. And 3 must be placed before 30.


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
