class Solution:
  # @param A : string
  # @return an integer
  def isPalindrome(self, A):
    high = len(A) - 1
    low = 0
    while low < high:
      if not A[low].isalnum():
        low += 1
        continue
      if not A[high].isalnum():
        high -= 1
        continue
      if A[low].lower() != A[high].lower():
        return 0
      low += 1
      high -= 1
    
    return 1

if __name__ == "__main__":
  sol = Solution()

  inputs = ["A man, a plan, a canal: Panama", "race a car"]
  expected_outputs = [1, 0]
  for idx, A in enumerate(inputs):
    result = sol.isPalindrome(A)
    print(f"Expected Result: {expected_outputs[idx]}.Actual Result:{result}")
  
  
