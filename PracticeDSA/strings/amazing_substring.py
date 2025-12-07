class Solution:
  # @param A : string
  # @return an integer
  def solve(self, A):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    count = 0
    for i in range(len(A)):
      if A[i] in vowels:
        count += len(A) - i
    return count % 10003

if __name__ == "__main__":
  sol = Solution()
  A = "ABEC"
  expected_output = 6
  result = sol.solve(A)
  print(f"Expected Result: {expected_output}.Actual Result:{result}")

