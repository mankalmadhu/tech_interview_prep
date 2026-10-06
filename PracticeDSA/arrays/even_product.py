#https://www.interviewbit.com/problems/even-product/
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        """
        Calculates the number of distinct operations to make the product of the array EVEN.

        Logic:
        1. Initial State: The problem states the initial product is ODD. This implies
           every single number in the array is currently Odd.
        2. Target State: To make a product EVEN, we need at least one Even number
           in the array.
        3. The Operation: We can choose *any* subset of indices and change their values.
           If we choose a non-empty subset, we can simply change those numbers to
           Even numbers, satisfying the condition.

        Combinatorics:
        - For an array of size n, the total number of possible subsets of indices
          is 2^n (the Power Set). Each element has 2 independent choices (include
          or exclude), so total subsets = 2 * 2 * ... * 2 (n times) = 2^n.
        - The only subset that DOES NOT work is the Empty Subset (choosing nothing),
          because the product would remain Odd.
        - Therefore, the answer is Total Subsets - Empty Subset = (2^n) - 1.

        Complexity Analysis:
        - (2**n) % MOD computes the full un-reduced 2**n first (astronomically
          large for big n) before reducing - this does more work as n grows than
          necessary. pow(2, n, MOD) (3-arg modular exponentiation) keeps every
          intermediate value bounded by MOD, giving O(log n) time, O(1) space
          regardless of how large n gets.
        """
        n = len(A)
        return ((2**n) - 1) % 1000000007


if __name__ == "__main__":
    sol = Solution()
    print(sol.solve([1, 3, 5]))  # expect 7
    print(sol.solve([1]))  # expect 1
    print(sol.solve([1, 1, 1, 1]))  # expect 15

    import random

    MOD = 1000000007
    for trial in range(300):
        n = random.randint(1, 1000)
        arr = [1] * n
        got = sol.solve(arr)
        expected = (pow(2, n, MOD) - 1) % MOD
        assert got == expected, f"Mismatch on n={n}: got {got}, expected {expected}"

    print("All stress tests passed!")
