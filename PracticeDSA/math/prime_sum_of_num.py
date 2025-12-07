class Solution:

  def primeSum(self, A):
    primes = self.build_prime_list(A)
    primaePairs = self.sum_primes_list(primes, A)
    return primaePairs[0] if primaePairs else []

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
    primesPairs = []
    while left <= right:
      if primes[left] + primes[right] == n:
        primesPairs.append((primes[left], primes[right]))
        left += 1
        right -= 1
      elif primes[left] + primes[right] < n:
        left += 1
      else:
        right -= 1

    if primesPairs:
      primesPairs.sort(key=lambda x: (x[0], x[1]))

    return primesPairs


if __name__ == "__main__":
  sol = Solution()
  A = [4, 10]
  expected_output = [[2, 2], [3, 7]]
  for idx, A in enumerate(A):
    result = sol.primeSum(A)
    print(f"Expected Result: {expected_output}.Actual Result:{result}")
