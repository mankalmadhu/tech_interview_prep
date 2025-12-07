#https://www.interviewbit.com/problems/woodcutting-made-easy/
class Solution:
  # @param A : list of integers
  # @param B : integer
  # @return an integer
  def solve(self, A, B):

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
