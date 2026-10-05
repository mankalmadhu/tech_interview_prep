"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/math/step_by_step.py until you're done.

Problem (Step By Step, InterviewBit):

https://www.interviewbit.com/problems/step-by-step/

You start at position 0 on a number line and want to reach target
A. On the i-th move, you must move exactly i positions (either
left or right, your choice). Return the minimum number of moves
required to reach exactly A.

Example:
  A = 2 -> output = 3  (e.g. +1 -2 +3 = 2)
  A = 3 -> output = 2  (e.g. +1 +2 = 3)

Write your solution below.
"""
import math

def min_steps(A):
    if A == 0:
        return A

    Abs_A =  abs(A)

    n = int((-1 + math.sqrt(1 + 8 * Abs_A)) / 2)

    while (n * (n + 1)) // 2 < Abs_A:
        n += 1


    while (n * (n + 1) // 2 - Abs_A) % 2 != 0:
        n += 1

    return n



if __name__ == "__main__":
    print(min_steps(2))  # expect 3
    print(min_steps(3))  # expect 2
    print(min_steps(0))  # expect 0
    print(min_steps(4))  # expect 3

    import random

    def brute_force_min_steps(target):
        # BFS over reachable sums, one level per step count
        if target == 0:
            return 0
        reachable = {0}
        n = 0
        while True:
            n += 1
            reachable = {r + n for r in reachable} | {r - n for r in reachable}
            if target in reachable:
                return n

    for trial in range(200):
        target = random.randint(0, 200)
        got = min_steps(target)
        expected = brute_force_min_steps(target)
        assert got == expected, f"Mismatch on {target}: got {got}, expected {expected}"
        got_neg = min_steps(-target)
        assert got_neg == expected, f"Mismatch on {-target}: got {got_neg}, expected {expected}"

    print("All stress tests passed!")
