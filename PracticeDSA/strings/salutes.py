class Solution:
  # @param A : string
   # @return an long
  def countSalutes(self, A):
    """
    Calculates the total number of salutes (crossings) in the hallway.

        Strategy: Linear Scan with State Tracking
        -----------------------------------------
        We iterate through the string once from left to right.
        - We maintain a counter `rightCount` for people walking Right (>).
        - When we encounter a person walking Left (<):
          - They are guaranteed to cross EVERY person walking Right that 
            we have seen so far (since those people are to their left and moving right).
          - We add `rightCount` to the total salutes.
        
        Complexity Analysis:
        --------------------
        Time Complexity: O(N)
           - Single pass through the string.
        Space Complexity: O(1)
           - Only integer counters are used.
    """
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
    