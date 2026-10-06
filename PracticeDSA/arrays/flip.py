# https://www.interviewbit.com/problems/flip/
class Solution:
    def flip(self, A: str) -> list[int]:
        """
        Finds the contiguous subarray to flip (0 to 1, 1 to 0) to maximize the total number of 1s.

        Algorithm: Kadane's Algorithm (Modified)
        - Time Complexity: O(N) where N is the length of the string A. We iterate through the string.
        - Space Complexity: O(N) to store the mapped `bit_arr`. (Note: Can be optimized to O(1) by evaluating `A[i]` on the fly inside the Kadane's loop).

        Example Trace for A = "010":
        - Mapping: '0' -> 1 (net gain), '1' -> -1 (net loss). The array conceptually becomes [1, -1, 1].
        - i = 0 (val = 1): cur_sum = 1. cur_sum > max_sum (-inf), so max_sum = 1, left = 0, right = 0.
        - i = 1 (val = -1): cur_sum = 0. max_sum remains 1.
        - i = 2 (val = 1): cur_sum = 1. max_sum remains 1. (Because cur_sum is not strictly > max_sum, we don't update the pointers, which correctly favors the lexicographically earliest subarray!)
        - Result: [left+1, right+1] -> [1, 1].
        """
        ans = []
        if "0" not in A:
            return ans

        bit_arr = []
        for i in range(len(A)):
            bit_val = 1 if A[i] == "0" else -1
            bit_arr.append(bit_val)

        cur_sum, max_sum = 0, float("-inf")
        start, left, right = 0, 0, 0

        for i in range(len(bit_arr)):
            cur_sum += bit_arr[i]

            if cur_sum > max_sum:
                max_sum = cur_sum
                right = i
                left = start

            if cur_sum < 0:
                cur_sum = 0
                start = i + 1

        ans.append(left + 1)
        ans.append(right + 1)

        return ans


if __name__ == "__main__":
    sol = Solution()
    inputs = ["010", "111", "0000", "1011000"]
    expected_outputs = [[1, 1], [], [1, 4], [5, 7]]

    for idx, A in enumerate(inputs):
        result = sol.flip(A)
        assert result == expected_outputs[idx], (
            f"A={A}: expected {expected_outputs[idx]}, got {result}"
        )
        print(f"Expected Result: {expected_outputs[idx]}. Actual Result: {result}")
    print("All example tests passed!")

    import random

    def ones_count_after_flip(A, l, r):
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
        got = Solution().flip(A)
        expected = brute_force(A)
        assert got == expected, f"Mismatch on A={A!r}: got {got}, expected {expected}"

    print("All stress tests passed!")
