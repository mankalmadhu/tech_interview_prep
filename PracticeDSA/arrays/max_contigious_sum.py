class Solution:
  # @param A : tuple of integers
  # @return an integer
  # https://www.interviewbit.com/problems/max-sum-contiguous-subarray/
  def maxSubArray(self, A):
    """
    The line cur_sum = max(A[i], cur_sum + A[i]) is necessary because at every step, it makes a crucial decision: should we extend the current subarray, or is it better to start a new one?

    Your simpler idea, cur_sum = cur_sum + A[i], would only calculate the sum of subarrays that always start from the very beginning of the array. It doesn't consider that the best subarray might start somewhere in the middle.

    The Two Choices at Every Step
    At every number A[i], you are making a choice:

    cur_sum + A[i]: This represents the choice to extend the best subarray found so far by adding the current number to it.

    A[i]: This represents the choice to discard the previous subarray and start a new subarray beginning only with the current number.

    Why You Need the Choice to Start Over
    You need this choice because sometimes the cur_sum up to the previous element becomes negative. A negative-sum prefix will always drag down the total value of any subarray that includes it. It's better to abandon that negative prefix and start fresh.

    Let's trace a simple example: A = [1, 2, -5, 4]

    i = 0: A[0] is 1.

    cur_sum is 1. max_sum is 1.

    i = 1: A[1] is 2.

    We compare cur_sum + A[1] (which is 1 + 2 = 3) with A[1] (which is 2).

    cur_sum becomes max(2, 3) = 3. We extend our subarray [1, 2].

    max_sum becomes max(1, 3) = 3.

    i = 2: A[2] is -5.

    We compare cur_sum + A[2] (which is 3 + -5 = -2) with A[2] (which is -5).

    cur_sum becomes max(-5, -2) = -2. We extend our subarray [1, 2, -5].

    max_sum is still 3.

    i = 3: A[3] is 4. (This is the key step)

    We compare cur_sum + A[3] (which is -2 + 4 = 2) with A[3] (which is 4).

    cur_sum becomes max(4, 2) = 4.

    Here, the algorithm chose to start a new subarray [4]. It was better than extending the old one, because the previous cur_sum of -2 was just dragging the total down.

    max_sum becomes max(3, 4) = 4.

    This max() check is the magic that allows the algorithm to cleverly discard negative-sum prefixes and find the optimal subarray, no matter where it begins.
    """

    if not A:
      return 0

    max_sum = A[0]
    cur_sum = A[0]
    for i in range(1, len(A)):
      cur_sum = max(A[i], cur_sum + A[i])
      max_sum = max(max_sum, cur_sum)

    return max_sum
