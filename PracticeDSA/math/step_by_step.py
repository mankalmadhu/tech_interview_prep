class Solution:
  # @param A : integer
  # @return an integer
  # https://www.interviewbit.com/problems/step-by-step/
  def solve(self, A):
    """
    Calculates the minimum steps to reach target A from 0.
        On the i-th step, you must move exactly i positions left or right.

        Strategy: Math + Parity Check
        -----------------------------
        1. Base Requirement: The sum of steps 1..n must be at least abs(A).
           Sum = n * (n + 1) / 2 >= target
           
        2. Optimization: We solve the quadratic equation n^2 + n - 2*target = 0 
           to find the approximate starting 'n' immediately.

        3. Parity Logic (The Crucial Step):
           - Let 'S' be the sum of steps 1..n.
           - We want to reach 'target' by assigning signs: ±1 ±2 ... ±n = target.
           - Changing a step 'k' from +k to -k reduces the sum S by 2k.
           - Since 2k is always EVEN, flipping signs only changes the total sum 
             by an even amount.
           - Therefore, we can only reach 'target' if the difference (S - target) 
             is an EVEN number.
           - If (S - target) is odd, we increment n until the difference becomes even.

        Complexity Analysis:
        --------------------
        Time Complexity: O(1) 
           - The quadratic formula gives the answer instantly. The fix-up loop runs 
             at most 2-3 times.
        Space Complexity: O(1).

        Example Trace (Target = 2):
        ---------------------------
        1. Find min n where Sum >= 2:
           - n=1: Sum=1. (Too small)
           - n=2: Sum=3. (3 >= 2. OK).
           
        2. Check Parity (Sum - Target):
           - Current Sum (3) - Target (2) = 1.
           - 1 is ODD. We cannot reach 2 from 3 by flipping signs.
           - Increment n -> 3.

        3. Next n (n=3):
           - New Sum = 1+2+3 = 6.
           - Diff = 6 - 2 = 4.
           - 4 is EVEN. (We can flip signs to subtract 4 from sum).
           - Logic: We need to subtract 4 total. Flip '2' to '-2' (change is 2*2=4).
           - Moves: +1 -2 +3 = 2.
        
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
