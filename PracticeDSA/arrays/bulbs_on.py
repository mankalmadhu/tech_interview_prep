class Solution:
  # @param A : list of integers
  # @return an integer
  # https://www.interviewbit.com/problems/bulbs/
  def bulbs(self, A):
    count = 0
    for i in range(len(A)):

      effective_value = A[i] if count % 2 == 0 else 1 - A[i]

      if effective_value == 0:
        count += 1

    return count


# [ 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1 ]
# [ 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
# [ 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1]
# [ 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
# [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

if __name__ == "__main__":
  sol = Solution()
  A = [1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1]
  print(sol.bulbs(A))
