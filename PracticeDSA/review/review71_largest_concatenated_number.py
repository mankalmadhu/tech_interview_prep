"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/arrays/largest_concatenated_number.py until you're done.

Problem (Largest Number):

https://www.interviewbit.com/problems/largest-number/

Given a list of non-negative integers A, arrange them so that when
concatenated together (as strings), they form the largest possible
number. Return the result as a string.

Example:
  A = [3, 30, 34, 5, 9]
  Output: "9534330"

  A = [0, 0]
  Output: "0"   (not "00")

Write your solution below.
"""
from functools import cmp_to_key

def largest_number(A):

    def adj_str_concat_comp(a,b):
        anb = str(a) + str(b)
        bna = str(b) + str(a)

        if anb > bna:
            return -1
        elif bna > anb:
            return 1
        else:
            return 0

    sorted_a = sorted(A, key=cmp_to_key(adj_str_concat_comp))

    result = "".join(map(str,sorted_a))

    if result and result[0] =="0" and result[-1]=="0":
        return result[0]

    return result


if __name__ == "__main__":
    inputs = [[3, 30, 34, 5, 9], [0, 0], [1], [10, 2]]
    expected_outputs = ["9534330", "0", "1", "210"]

    for idx, A in enumerate(inputs):
        result = largest_number(A)
        assert result == expected_outputs[idx], (
            f"A={A}: expected {expected_outputs[idx]}, got {result}"
        )
        print(f"Expected Result: {expected_outputs[idx]}. Actual Result: {result}")
    print("All example tests passed!")

    import random
    from itertools import permutations

    def brute_force(A):
        best = None
        for perm in permutations(A):
            candidate = "".join(map(str, perm))
            if best is None or candidate > best:
                best = candidate
        if best and best[0] == "0":
            return "0"
        return best if best is not None else ""

    for trial in range(200):
        n = random.randint(0, 6)
        A = [random.randint(0, 50) for _ in range(n)]
        got = largest_number(A[:])
        expected = brute_force(A[:])
        assert got == expected, f"Mismatch on {A}: got {got}, expected {expected}"

    print("All stress tests passed!")
