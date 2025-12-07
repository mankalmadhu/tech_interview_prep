class Solution:
  # @param A : list of integers
  # @return a list of integers
  def findOccurences(self, A):
    A.sort()
    result_dict = {}
    for num in A:
      if num in result_dict:
        result_dict[num] += 1
      else:
        result_dict[num] = 1
    return result_dict.values()
