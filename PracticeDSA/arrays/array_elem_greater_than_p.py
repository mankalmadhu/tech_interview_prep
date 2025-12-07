class Solution:
  # @param A : list of integers
  # @return an integer
  # https://www.interviewbit.com/problems/array-elements-greater-than-p/
  def solve(self, A):

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

