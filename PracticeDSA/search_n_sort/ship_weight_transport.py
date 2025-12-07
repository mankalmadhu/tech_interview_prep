class Solution:
  # @param A : list of integers
  # @param B : integer
  # @return an integer
  def solve(self, A, B):
      """
      The overall time complexity is determined by the combination of two parts: the binary search and the canShipWeight helper function.
      Binary Search: The while loop runs a logarithmic number of times. The search space is from max(A) to sum(A). In the worst case, the number of iterations is log(sum(A)−max(A)), which can be simplified to O(logS).
      canShipWeight Function: Inside each iteration of the binary search, this function is called. It iterates through all packages once to determine if a given capacity is feasible. This takes O(N) time, where N is the number of packages.
      Since the O(N) operation is performed inside the O(logS) loop, we multiply the two complexities together.

      Time Complexity=O(logS)×O(N)=O(NlogS)
      """
      low, high = max(A), sum(A)

      globalMin = float('inf')

      while low <= high:
          mid = (low + high)//2
          if self.canShipWeight(A,B, mid):
              globalMin = min(globalMin, mid)
              high = mid-1
          else:
              low = mid + 1

      return globalMin

  def canShipWeight(self, A, B, capacity):
      days = 1
      cur_capacity = 0

      for weight in A:
          if weight > capacity:
              return False
          if weight + cur_capacity <= capacity:
              cur_capacity += weight
          else:
              days +=1
              cur_capacity = weight

          if days > B:
              return False

      return True



if __name__ == "__main__":
    sol = Solution()
    AsInput = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [3, 2, 2, 4, 1, 4]]
    BsInput = [5, 3]
    expected_output = [15, 6]

    for idx, A in enumerate(AsInput):
        result = sol.solve(A, BsInput[idx])
        print(f"Expected Result: {expected_output[idx]}.Actual Result:{result}")