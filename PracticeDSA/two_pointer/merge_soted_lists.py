class Solution:
  # @param A : list of integers
  # @param B : list of integers
  def merge(self, A, B):
      m = len(A)
      n = len(B)
      i = m - 1
      j = n - 1
      k = m + n - 1

      # Extend A to accommodate all elements from B
      A.extend([0] * n)

      # Merge from the end, handling negative numbers properly
      while i >= 0 and j >= 0:
          if A[i] > B[j]:
              A[k] = A[i]
              i -= 1
          else:
              A[k] = B[j]
              j -= 1
          k -= 1

      # Copy remaining elements from B (if any)
      while j >= 0:
          A[k] = B[j]
          j -= 1
          k -= 1
     
        

if __name__ == "__main__":
  sol = Solution()
  A = [1, 5, 8]
  B = [6, 9]
  expected = [1, 5, 6, 8, 9]
  sol.merge(A, B)
  print(A, expected)

