class Solution:
  # @param A : list of integers
  # @param B : integer
  # @return an integer
  def threeSumClosest(self, A, B):
    """
    This implementation is a standard and efficient way to solve the 3-Sum Closest problem. It has a time complexity of O(N^2) due to the nested loops, which is optimal for this problem.
    """
    A.sort()
    closest_sum = float('inf')
    n = len(A)

    for i in range(n - 2):

      left = i + 1
      right = n - 1

      while left < right:
        current_sum = A[i] + A[left] + A[right]
        if (abs(current_sum - B) < abs(closest_sum - B)):
          closest_sum = current_sum
        if current_sum < B:
          left += 1
        elif current_sum > B:
          right -= 1
        else:
          break

    return closest_sum


if __name__ == "__main__":
  sol = Solution()
  As = [[-1, 2, 1, -4], [1, 2, 3],
        [2147483647, -2147483648, -2147483648, 0, 1]]
  Bs = [1, 6, 0]
  expected_outputs = [2, 6, 0]
  for idx, A in enumerate(As):
    result = sol.threeSumClosest(A, Bs[idx])
    print(f"Expected Result: {expected_outputs[idx]}.Actual Result:{result}")
