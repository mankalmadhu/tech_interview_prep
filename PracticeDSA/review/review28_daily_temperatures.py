"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/stacks/daily_temperatures.py until you're done.

Problem (Daily Temperatures, LeetCode 739):

Given an array of daily temperatures, return an array `answer` such
that `answer[i]` is the number of days you have to wait after day i
to get a warmer temperature. If there is no future day for which
this is possible, put 0 instead.

Example:
  temperatures = [73,74,75,71,69,72,76,73]
  -> [1,1,4,2,1,1,0,0]

Write your solution below (monotonic decreasing stack of indices, O(N)).
"""


class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                result[prev] = i - prev

            stack.append(i)

        return result




if __name__ == "__main__":
    sol = Solution()
    fixed_cases = [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([30, 30, 30], [0, 0, 0]),
        ([], []),
        ([50], [0]),
    ]
    for temps, expected in fixed_cases:
        got = sol.dailyTemperatures(temps)
        assert got == expected, f"{temps}: expected {expected}, got {got}"
    print("fixed cases passed")

    import random

    def brute_force(temps):
        n = len(temps)
        ans = [0] * n
        for i in range(n):
            for j in range(i + 1, n):
                if temps[j] > temps[i]:
                    ans[i] = j - i
                    break
        return ans

    for _ in range(1000):
        n = random.randint(0, 20)
        temps = [random.randint(30, 100) for _ in range(n)]
        got = sol.dailyTemperatures(temps)
        want = brute_force(temps)
        assert got == want, f"{temps}: expected {want}, got {got}"
    print("1000 randomized trials passed")
