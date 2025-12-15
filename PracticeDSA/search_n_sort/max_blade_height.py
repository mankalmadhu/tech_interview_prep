#https://www.interviewbit.com/problems/woodcutting-made-easy/
class Solution:
  # @param A : list of integers
  # @param B : integer
  # @return an integer
  def solve(self, A, B):
    """
    Finds the maximum blade height to collect at least B units of wood.

        Problem Context (EKO / Woodcutting):
        ------------------------------------
        - We have trees of various heights in array A.
        - A machine cuts trees at a fixed height H.
        - Any part of a tree higher than H is cut off and collected.
        - Goal: Maximize H such that sum(cut_parts) >= B.

        Strategy: Binary Search on Answer
        ---------------------------------
        The amount of wood collected is inversely proportional to the blade height H.
        - Higher H -> Less Wood.
        - Lower H -> More Wood.
        This monotonicity allows Binary Search.

        1. Range: Low = 0, High = max(A).
        2. Check(mid): Calculate wood collected if blade is at height 'mid'.
        3. Decision:
           - If wood >= B: This height works! We record it as a possible answer.
             But we want to save more tree, so we try a HIGHER blade (move low -> mid + 1).
           - If wood < B: Not enough wood. We MUST lower the blade (move high -> mid - 1).

        Complexity Analysis:
        --------------------
        Time Complexity: O(N * log(max(A)))
           - Search space is 0 to max(A). Binary Search takes O(log(max(A))).
           - Each step requires O(N) to calculate collected wood.
        Space Complexity: O(1)
           - Constant extra space.
    """

    low = 0
    high = max(A)
    maxBladeHeight = 0

    while low <= high:
      mid = (low + high) // 2
      woodCollected = 0

      for i in range(len(A)):
        if A[i] > mid:
          woodCollected += A[i] - mid

      if woodCollected >= B:
        low = mid + 1
        maxBladeHeight = mid
      else:
        high = mid - 1

    return maxBladeHeight


if __name__ == "__main__":
  sol = Solution()
  A = [[20, 15, 10, 17], [4, 42, 40, 26, 46]]
  B = [7, 20]
  expcted_output = [15, 36]
  for idx, a in enumerate(A):
    result = sol.solve(a, B[idx])
    print(f"Expected Result: {expcted_output[idx]}.Actual Result:{result}")
