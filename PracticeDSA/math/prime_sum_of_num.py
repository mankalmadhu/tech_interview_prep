class Solution:

  def primeSum(self, A):
    """
    Returns two prime numbers whose sum is exactly A.
    Returns the lexicographically smallest pair.

    Complexity Analysis:
    --------------------
    - Sieve of Eratosthenes: O(N log(log N)) Time | O(N) Space
    - Two-Pointer Search: O(P) Time | O(1) Space (where P is number of primes <= A)
    """
    primes = self.build_prime_list(A)
    return self.sum_primes_list(primes, A)

  def build_prime_list(self, n):
    if n < 2:
      return []

    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers.

    for i in range(2, int(n**0.5) + 1):
      if is_prime[i]:
        # Mark all multiples of i (except i itself) as not prime.
        for multiple in range(i * i, n, i):
          is_prime[multiple] = False

    primes = []
    for i in range(n):
      if is_prime[i]:
        primes.append(i)

    return primes

  def sum_primes_list(self, primes, n):
    left = 0
    right = len(primes) - 1
    while left <= right:
      if primes[left] + primes[right] == n:
        return [primes[left], primes[right]]
      elif primes[left] + primes[right] < n:
        left += 1
      else:
        right -= 1
    return []


if __name__ == "__main__":
  sol = Solution()
  A = [4, 10]
  expected_output = [[2, 2], [3, 7]]
  for idx, A in enumerate(A):
    result = sol.primeSum(A)
    print(f"Expected Result: {expected_output}.Actual Result:{result}")
