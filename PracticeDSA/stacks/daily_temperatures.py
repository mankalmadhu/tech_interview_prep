class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """
        Calculates the number of days you have to wait after each day to get a warmer temperature.

        Algorithm: Monotonic Decreasing Stack
        - Time Complexity: O(N) amortized. Each index is pushed onto the stack exactly once
          and popped at most once.
        - Space Complexity: O(N) in the worst case (strictly decreasing temperatures)
          where no elements are popped, causing the stack to grow to size N.

        Design Trade-offs & Logic:
        - We maintain a stack of indices representing days that haven't found a warmer day yet.
        - The stack invariant is strictly decreasing temperature values.
        - When a warmer day `temperatures[i]` is encountered, we repeatedly pop the colder
          days from the stack, resolving their waiting time as `i - popped_index`.
        """
        n = len(temperatures)
        result = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            stack.append(i)
        return result


if __name__ == "__main__":
    sol = Solution()
    print(
        "Test 1: [73,74,75,71,69,72,76,73] -> Expected: [1,1,4,2,1,1,0,0], Got:",
        sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]),
    )
    print(
        "Test 2: [30,40,50,60]             -> Expected: [1,1,1,0], Got:",
        sol.dailyTemperatures([30, 40, 50, 60]),
    )
    print(
        "Test 3: [30,30,30]                -> Expected: [0,0,0], Got:",
        sol.dailyTemperatures([30, 30, 30]),
    )
    print("All tests executed!")

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
