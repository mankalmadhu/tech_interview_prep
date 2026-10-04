"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/math/power_of_two_ints.py until you're done.

Problem (Power of Two Integers / Valid Perfect Power):

Given a positive integer A, determine whether it can be expressed as
x^y where x and y are integers greater than 1 (x > 1, y > 1).
Return 1 if true, 0 otherwise.

Example:
  A = 16 -> 1 (2^4 or 4^2)
  A = 10 -> 0 (no valid x, y)
  A = 1  -> 0 (no valid x, y > 1 exists since 1^anything = 1, needs y>1 but x must be >1 too)

Write your solution below.
"""

from math import sqrt, log, ceil, floor

def is_power_of_two_ints(a):
    if a == 1:
        return 0
    for i in range(2, int(sqrt(a)+1)):
        log_val = log(a,i)
        if i ** round(log_val) == a:
            return 1

    return 0




if __name__ == "__main__":
    print(is_power_of_two_ints(16))  # expect 1
    print(is_power_of_two_ints(10))  # expect 0
    print(is_power_of_two_ints(1))  # expect 0

    assert is_power_of_two_ints(16) == 1
    assert is_power_of_two_ints(10) == 0
    assert is_power_of_two_ints(1) == 0
    assert is_power_of_two_ints(512) == 1  # 8^3
    assert is_power_of_two_ints(2) == 0  # prime, no valid x,y>1
    assert is_power_of_two_ints(4) == 1  # 2^2
    assert is_power_of_two_ints(2401) == 1  # 7^4
    print("fixed cases passed")

    import random

    def brute_force(a):
        for x in range(2, int(a**0.5) + 2):
            y = 2
            val = x**y
            while val < a:
                y += 1
                val = x**y
            if val == a:
                return 1
        return 0

    for n in range(1, 2000):
        got = is_power_of_two_ints(n)
        want = brute_force(n)
        assert got == want, f"n={n}: expected {want}, got {got}"
    print("exhaustive 1..2000 trials passed")
