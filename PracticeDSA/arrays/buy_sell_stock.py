class Solution:
    """
    Calculates the maximum profit achievable from a single buy and sell transaction.

    Time Complexity: O(N)
    - We iterate through the 'prices' array exactly once.

    Space Complexity: O(1)
    - We only track two variables: 'min_val' and 'max_profit'.

    Logic & Trade-offs:
    - We maintain the lowest price seen so far ('min_val') and the maximum
      profit calculated up to the current day.
    - At each day, we first update 'min_val' if the current price is lower.
    - Then, we check if selling at the current price (minus our historical 'min_val')
      yields a higher profit than our recorded 'max_profit'.
    - Initializing 'min_val' to float('inf') elegantly handles empty array edge cases
      without requiring an explicit guard clause like `if not prices: return 0`.
    """

    def maxProfit(self, prices: list[int]) -> int:

        min_val = float("inf")
        max_profit = 0

        for price in prices:
            if min_val > price:
                min_val = price
            if max_profit < price - min_val:
                max_profit = price - min_val

        return max_profit


def _brute_force_profit(prices):
    best = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            best = max(best, prices[j] - prices[i])
    return best


if __name__ == "__main__":
    sol = Solution()
    print(
        "Test 1: [7,1,5,3,6,4] -> Expected: 5, Got:", sol.maxProfit([7, 1, 5, 3, 6, 4])
    )
    print("Test 2: [7,6,4,3,1]   -> Expected: 0, Got:", sol.maxProfit([7, 6, 4, 3, 1]))
    print("Test 3: [2,4,1]       -> Expected: 2, Got:", sol.maxProfit([2, 4, 1]))
    print("All tests executed!")

    import random

    for trial in range(300):
        n = random.randint(0, 50)
        prices = [random.randint(1, 100) for _ in range(n)]
        got = sol.maxProfit(prices)
        expected = _brute_force_profit(prices)
        assert got == expected, f"Mismatch on {prices}: got {got}, expected {expected}"

    print("All stress tests passed!")
