class Solution:
  # @param A : string
   # @return an long
  def countSalutes(self, A):
      rightCount = 0
      totalSalutes = 0

      for person in A:
        if person == '>':
          rightCount += 1
        elif person == '<':
          totalSalutes += rightCount
      return totalSalutes

    
    
  def countSalutes_n2(self, A):
    count = 0
    for ldx,right in enumerate(A):
      if right == '>':
        for hdx,left in enumerate(A[::-1]):
          if left == '<' and (hdx > ldx):
            count += 1

    return count

if __name__ == "__main__":
  sol = Solution()
  inputs = [">>><<<", "<>"]
  expected_outputs = [9, 0]
  for idx, A in enumerate(inputs):
    result = sol.countSalutes(A)
    print(f"Expected Result: {expected_outputs[idx]}.Actual Result:{result}")
    