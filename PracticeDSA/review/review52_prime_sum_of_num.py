"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/math/prime_sum_of_num.py until you're done.

Problem (Prime Sum / Goldbach's Conjecture):

Given an even number A (greater than 2), return two prime numbers
whose sum is equal to the given number. If multiple solutions
exist, return any one of them.

Example:
  A = 4 -> [2, 2]
  A = 10 -> [3, 7] (or [5, 5])

Write your solution below.
"""


def prime_sum(a):
    return sum_primes(a, build_prime_list(a))

def build_prime_list(a):
    if a < 2:
        return []

    is_prime = [True] * a

    is_prime[0], is_prime[1] = False, False

    for i in range(2, int(a**0.5)+1):
        if(is_prime[i]):
            for j in range(i*i, a,i):
                is_prime[j] = False

    prime_list = []
    for i in range(len(is_prime)):
        if is_prime[i]:
            prime_list.append(i)

    return prime_list

def sum_primes(a, prime_list):
    l = 0
    r = len(prime_list) - 1

    while l <= r:
        if prime_list[l] + prime_list[r] == a:
            return [prime_list[l], prime_list[r]]
        elif prime_list[l] + prime_list[r] < a :
            l += 1
        else:
            r -= 1
    return []


if __name__ == "__main__":
    print(prime_sum(4))  # expect a pair of primes summing to 4, e.g. [2, 2]
    print(prime_sum(10))  # expect a pair of primes summing to 10
    print(prime_sum(100))  # expect a pair of primes summing to 100

    def is_prime_slow(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def check_valid(a, pair):
        assert len(pair) == 2, f"a={a}: expected a pair, got {pair}"
        p, q = pair
        assert p + q == a, f"a={a}: {p}+{q} != {a}"
        assert is_prime_slow(p), f"a={a}: {p} is not prime"
        assert is_prime_slow(q), f"a={a}: {q} is not prime"

    check_valid(4, prime_sum(4))
    check_valid(10, prime_sum(10))
    check_valid(100, prime_sum(100))
    print("fixed cases passed")

    for a in range(4, 2000, 2):
        check_valid(a, prime_sum(a))
    print("exhaustive even 4..1998 trials passed")
