"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/arrays/flip.py until you're done.

Problem (Flip):

https://www.interviewbit.com/problems/flip/

You are given a binary string A (containing only '0'/'1'). You can choose
one contiguous subarray [L, R] (1-indexed) and flip every bit in it
(0 -> 1 and 1 -> 0). Find the L, R (1-indexed, inclusive) that maximizes
the total number of 1s in the resulting string.

If no flip can increase the number of 1s (e.g. the string is all 1s, or
empty), return an empty list.

If multiple answers exist, return the one with the smallest L; if still
tied, smallest R.

Example:
  A = "010"
  Output: [1, 1]   (flip just index 1: "010" -> "110", gain of 1)

  A = "111"
  Output: []  (flipping anything only decreases 1-count)

Write your solution below.
"""


def flip(A):

    if not A or "0" not in A:
        return []

    bit_arr = [1 if i=="0" else -1 for i in A]

    cur_sum, max_sum = 0 , float('-inf')
    left, right , start = 0, 0, 0
    ans = []

    for i in range(len(bit_arr)):

        cur_sum += bit_arr[i]

        if cur_sum > max_sum:
            max_sum = cur_sum
            left = start
            right = i

        if cur_sum < 0:
            cur_sum = 0
            start = i+1

    ans.append(left+1)
    ans.append(right+1)

    return ans


if __name__ == "__main__":
    inputs = ["010", "111", "0000", "1011000"]
    expected_outputs = [[1, 1], [], [1, 4], [5, 7]]

    for idx, A in enumerate(inputs):
        result = flip(A)
        assert result == expected_outputs[idx], (
            f"A={A}: expected {expected_outputs[idx]}, got {result}"
        )
        print(f"Expected Result: {expected_outputs[idx]}. Actual Result: {result}")
    print("All example tests passed!")

    import random

    def ones_count_after_flip(A, l, r):
        # l, r are 1-indexed inclusive
        count = 0
        for i, ch in enumerate(A):
            pos = i + 1
            bit = ch
            if l <= pos <= r:
                bit = "1" if ch == "0" else "0"
            if bit == "1":
                count += 1
        return count

    def brute_force(A):
        n = len(A)
        base_ones = A.count("1")
        best_gain = 0
        best = []
        for l in range(1, n + 1):
            for r in range(l, n + 1):
                gain = ones_count_after_flip(A, l, r) - base_ones
                if gain > best_gain:
                    best_gain = gain
                    best = [l, r]
        return best

    for trial in range(300):
        n = random.randint(0, 10)
        A = "".join(random.choice("01") for _ in range(n))
        got = flip(A)
        expected = brute_force(A)
        assert got == expected, f"Mismatch on A={A!r}: got {got}, expected {expected}"

    print("All stress tests passed!")
