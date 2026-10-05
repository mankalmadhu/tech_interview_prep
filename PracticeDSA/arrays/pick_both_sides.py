class Solution:
    # https://www.interviewbit.com/problems/pick-from-both-sides/
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        max_sum = 0

        if len(A) < B:
            return max_sum

        cur_sum = sum(A[0:B])
        max_sum = cur_sum

        for i in range(B):
            cur_sum -= A[B - 1 - i]
            cur_sum += A[len(A) - 1 - i]
            max_sum = max(max_sum, cur_sum)

        return max_sum


def _brute_force_pick(A, B):
    n = len(A)
    if n < B or B == 0:
        return 0
    best = None
    for k in range(B + 1):
        front = sum(A[:k]) if k > 0 else 0
        back = sum(A[n - (B - k):]) if (B - k) > 0 else 0
        total = front + back
        if best is None or total > best:
            best = total
    return best


if __name__ == "__main__":
    sol = Solution()
    print(sol.solve([5, -2, 3, 1, 2], 3))  # expect 8
    print(sol.solve([1, 2, 3, 4, 5], 3))  # expect 12
    print(sol.solve([1, 1, 1, 1, 1], 5))  # expect 5

    import random

    for trial in range(300):
        n = random.randint(1, 20)
        arr = [random.randint(-10, 10) for _ in range(n)]
        B = random.randint(0, n)
        got = sol.solve(arr, B)
        expected = _brute_force_pick(arr, B)
        assert got == expected, f"Mismatch on {arr}, B={B}: got {got}, expected {expected}"

    print("All stress tests passed!")
