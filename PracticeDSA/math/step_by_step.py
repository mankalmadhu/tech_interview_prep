class Solution:
  # @param A : integer
  # @return an integer
  # https://www.interviewbit.com/problems/step-by-step/
  def solve(self, A):

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
