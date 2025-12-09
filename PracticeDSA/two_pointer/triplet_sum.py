class Solution:
  # @param A : list of integers
  # @param B : integer
  # @return an integer
  def threeSumClosest(self, A, B):
  """
  Finds the sum of three integers in A such that the sum is closest to B.

        Strategy: Sorting + Two Pointers
        --------------------------------
        1. Sort the array. This allows us to make intelligent decisions about 
           how to adjust the sum (increase or decrease) by moving pointers.
        2. Iterate with a fixed first element 'A[i]'.
        3. Use Two Pointers for the remaining part (left = i + 1, right = n - 1).
        4. Calculate 'current_sum = A[i] + A[left] + A[right]'.
        5. Compare 'current_sum' with 'B':
           - If closer to B than our recorded 'closest_sum', update 'closest_sum'.
           - If current_sum < B: We need a larger sum -> Move left pointer right.
           - If current_sum > B: We need a smaller sum -> Move right pointer left.
           - If current_sum == B: Exact match found, return B immediately.

        Complexity Analysis:
        --------------------
        Time Complexity: O(N^2)
           - Sorting takes O(N log N).
           - The main loop runs N times. Inside, the two pointers traverse the 
             rest of the array once (O(N)). Total = O(N^2).
           - O(N^2) dominates O(N log N).
        
        Space Complexity: O(1)
           - We use pointers and simple variables. (Ignoring sort stack space).
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
