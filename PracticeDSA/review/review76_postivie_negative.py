"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/arrays/postivie_negative.py until you're done.

Problem (Positive Negative):

https://www.interviewbit.com/problems/positive-negative/

Given an integer array A, count the number of positive and negative
elements (ignore zeros). Return [count_positives, count_negatives].

Example:
  A = [1, 0, -1]
  Output: [1, 1]

Write your solution below.
"""


def solve(A):
    # TODO: implement
    pos_count = 0
    neg_count = 0
    for num in A:
       if num > 0:
           pos_count +=1
       elif num <0:
           neg_count +=1

    return [pos_count, neg_count]



if __name__ == "__main__":
    inputs = [[1, 0, -1], [], [1, 2, 3], [-1, -2], [0, 0, 0]]
    expected_outputs = [[1, 1], [0, 0], [3, 0], [0, 2], [0, 0]]

    for idx, A in enumerate(inputs):
        result = solve(A)
        assert result == expected_outputs[idx], (
            f"A={A}: expected {expected_outputs[idx]}, got {result}"
        )
        print(f"Expected Result: {expected_outputs[idx]}. Actual Result: {result}")
    print("All example tests passed!")

    import random

    for trial in range(200):
        n = random.randint(0, 20)
        A = [random.randint(-5, 5) for _ in range(n)]
        got = solve(A)
        expected = [sum(1 for x in A if x > 0), sum(1 for x in A if x < 0)]
        assert got == expected, f"Mismatch on {A}: got {got}, expected {expected}"

    print("All stress tests passed!")
