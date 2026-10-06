"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/arrays/array_elem_greater_than_p.py until you're done.

Problem (Noble Integer):

https://www.interviewbit.com/problems/noble-integer/

Given an integer array A, find if an integer p exists in the array such that
the number of integers strictly greater than p in the array equals p.

Return 1 if such an integer exists, else return -1.

(The original file in this repo generalizes this to count ALL such noble
integers, returning the count, or -1 if none exist. Feel free to start with
the simpler single-boolean version, then extend to counting if you'd like.)

Example:
  A = [3, 2, 1, 3]
  -> there's an integer 2, and there are exactly 2 elements greater than it
     (3 and 3) -> answer: 1 (found)

  A = [1, 1, 3, 3]
  -> no integer p has exactly p elements greater than it -> answer: -1

Write your solution below.
"""


def solve(A):
    A.sort()
    count = 0
    n =  len(A)

    for i in range(n):
        if i < n-1 and A[i] == A[i+1]:
            continue
        if A[i] == n-i-1:
            count +=1

    return count if count > 0 else -1




if __name__ == "__main__":
    inputs = [[3, 2, 1, 3], [1, 1, 3, 3]]
    expected_outputs = [1, -1]

    for idx, A in enumerate(inputs):
        result = solve(A)
        assert result == expected_outputs[idx], (
            f"A={A}: expected {expected_outputs[idx]}, got {result}"
        )
        print(f"Expected Result: {expected_outputs[idx]}. Actual Result: {result}")
    print("All example tests passed!")

    import random

    def brute_force(A):
        n = len(A)
        seen_values = set()
        count = 0
        for p in A:
            if p in seen_values:
                continue
            seen_values.add(p)
            greater_count = sum(1 for x in A if x > p)
            if greater_count == p:
                count += 1
        return count if count > 0 else -1

    for trial in range(300):
        n = random.randint(0, 15)
        A = [random.randint(0, 10) for _ in range(n)]
        got = solve(A[:])
        expected = brute_force(A[:])
        assert got == expected, f"Mismatch on {A}: got {got}, expected {expected}"

    print("All stress tests passed!")
