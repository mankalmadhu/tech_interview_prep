"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/arrays/max_psotitive_sum.py until you're done.

Problem (Max Non Negative SubArray):

https://www.interviewbit.com/problems/max-non-negative-subarray/

Given an array of integers (may include negatives), find the contiguous
subarray that contains only non-negative integers and has the maximum
possible sum. Return the subarray itself (as a list), not just the sum.

Tie-breaking rules, in order:
  1. Larger sum wins.
  2. If sums are equal, the longer subarray wins.
  3. If sums and lengths are equal, the one starting earliest wins.

If there is no non-negative element at all, return an empty list.

Example:
  A = [1, 2, 5, -7, 2, 3]
  Output: [1, 2, 5]   (sum=8, beats [2, 3] which sums to 5)

Write your solution below.
"""


def maxset(A):

    if not A:
        return []

    max_sum_start = 0
    max_sum_end = 0
    max_sum = float('-inf')
    segment_start = 0

    cur_sum = 0

    for i in range(len(A)):
         if A[i] < 0:
             cur_sum = 0
             segment_start = i+1
             continue


         cur_sum += A[i]
         if cur_sum > max_sum:
             max_sum = cur_sum
             max_sum_start = segment_start
             max_sum_end = i

         if cur_sum == max_sum:
             sub_array_len = i - segment_start
             best_sub_array_len = max_sum_end - max_sum_start

             if (sub_array_len > best_sub_array_len) or \
             ( (sub_array_len == best_sub_array_len) and segment_start < max_sum_start):
                 max_sum_start =  segment_start
                 max_sum_end = i

    if max_sum == float('-inf'):
        return []

    return A[max_sum_start: max_sum_end+1]






if __name__ == "__main__":
    inputs = [
        [1, 2, 5, -7, 2, 3],
        [-1, -2, -3],
        [0, 0, -1, 0],
        [1, 2, -3, 4, 5],
        [],
    ]
    expected_outputs = [
        [1, 2, 5],
        [],
        [0, 0],
        [4, 5],
        [],
    ]

    for idx, A in enumerate(inputs):
        result = maxset(A)
        assert result == expected_outputs[idx], (
            f"A={A}: expected {expected_outputs[idx]}, got {result}"
        )
        print(f"Expected Result: {expected_outputs[idx]}. Actual Result: {result}")
    print("All example tests passed!")

    import random

    def brute_force(A):
        n = len(A)
        best_sum = None
        best_start, best_end = 0, -1
        i = 0
        while i < n:
            if A[i] < 0:
                i += 1
                continue
            start = i
            seg_sum = 0
            while i < n and A[i] >= 0:
                seg_sum += A[i]
                i += 1
            end = i - 1
            seg_len = end - start
            if best_sum is None or seg_sum > best_sum:
                best_sum = seg_sum
                best_start, best_end = start, end
            elif seg_sum == best_sum:
                best_len = best_end - best_start
                if seg_len > best_len or (seg_len == best_len and start < best_start):
                    best_start, best_end = start, end
        if best_sum is None:
            return []
        return A[best_start:best_end + 1]

    for trial in range(300):
        n = random.randint(0, 15)
        A = [random.randint(-5, 5) for _ in range(n)]
        got = maxset(A[:])
        expected = brute_force(A[:])
        assert got == expected, f"Mismatch on {A}: got {got}, expected {expected}"

    print("All stress tests passed!")
