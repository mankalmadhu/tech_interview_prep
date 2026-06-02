class Solution:
  # @param A : integer
  # @return an integer
  # https://www.interviewbit.com/problems/step-by-step/
  def solve(self, A):
    """
    Calculates the minimum steps to reach target A from 0.
    On the i-th step, you must move exactly i positions left or right.

    Essence of the Algorithm:
    -------------------------
    1. If we were to only move in the positive direction, it suffices to find the 
       number of steps using the natural sum formula: n * (n + 1) // 2.
    2. Since we have the option to move in the negative direction, we first calculate 
       the quadratic root for the equation: n * (n + 1) // 2 <= target to get a baseline 'n'.
    3. We increment 'n' in a while loop to ensure our sum just reaches or overshoots the target.
    4. Now since we overshot, we must find a step 'k' to flip to the negative direction. 
       Because flipping a step from +k to -k reduces our total sum by exactly 2k 
       (which is always an EVEN amount), the difference between our total sum and 
       the target MUST be even.
    5. If the difference is odd, we keep incrementing our total steps 'n' until the 
       difference becomes even. The first 'n' that satisfies this condition is guaranteed 
       to be the minimum number of steps, because we test 'n' in monotonically increasing order.

    Complexity Analysis:
    --------------------
    Time Complexity: O(1) effectively (quadratic formula gives near-instant answer).
    Space Complexity: O(1)

    Example Trace (Target = 2):
    ---------------------------
    1. Base 'n' where Sum >= 2:
       - n=1: Sum=1. (Too small)
       - n=2: Sum=3. (3 >= 2. OK).
       
    2. Check Parity (Sum - Target):
       - Current Sum (3) - Target (2) = 1.
       - 1 is ODD. We cannot hit exactly 2 because flipping any step subtracts an EVEN amount.
       - Increment n -> 3.

    3. Next 'n' (n=3):
       - New Sum = 1+2+3 = 6.
       - Diff = 6 - 2 = 4.
       - 4 is EVEN. (We can mathematically flip a step to subtract exactly 4).
       - Logic: We need to subtract 4. Flipping step 'k' subtracts 2k. So 2k = 4 -> k = 2.
       - Verify by flipping step 2 to negative: +1 - 2 + 3 = 2. Target reached!
    
    Result: 3 steps.
    """

    if A == 0:
      return 0

    target = abs(A)

    import math
    # n * (n + 1) // 2 >= target, this is the formula for finding root of the quadratic equation 
    n = int((-1 + math.sqrt(1 + 8 * target)) / 2)

    while (n * (n+1))//2 < target:      
      n += 1    

    while (n * (n + 1) // 2 - target) % 2 != 0:
      n += 1     

    return n



if __name__ == "__main__":
  sol = Solution()
  A = [2,3, 4, 5, 6, 7, 8,9,10,11,12,13,14,15,16,17,18,19,20,21]
  expected_output = [3,2, 3, 5, 3, 5, 4,5,4,5,7,5,7,5,7,6,7,6,7,6]
  for idx, aS in enumerate(A):
    result = sol.solve(aS)
    print(f"For input :{aS}, Expected Result: {expected_output[idx]}.Actual Result:{result}")
