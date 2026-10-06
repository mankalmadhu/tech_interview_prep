"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/arrays/bulbs_on.py until you're done.

Problem (Bulbs):

https://www.interviewbit.com/problems/bulbs/

You have N light bulbs in a row, each on (1) or off (0). Pressing the
switch of the i-th bulb toggles the state of itself AND all bulbs to its
right. Find the minimum number of switch presses needed so that all
bulbs end up ON. You can press the same switch multiple times (though it
will never help to do so more than once).

Example:
  A = [0, 1, 0, 1]
  Output: 4
  (press 0 -> [1,0,1,0], press 1 -> [1,1,0,1],
   press 2 -> [1,1,1,0], press 3 -> [1,1,1,1])

Write your solution below.
"""


def bulbs(A):
    # TODO: implement
    flips = 0
    for  i in range(len(A)):
        cur_state =  A[i] if flips % 2 == 0 else 1-A[i]

        if cur_state == 0:
            flips += 1

    return flips



if __name__ == "__main__":
    inputs = [[0, 1, 0, 1], [1, 1, 1, 1], [0, 0, 0, 0]]
    expected_outputs = [4, 0, 1]

    for idx, A in enumerate(inputs):
        result = bulbs(A)
        assert result == expected_outputs[idx], (
            f"A={A}: expected {expected_outputs[idx]}, got {result}"
        )
        print(f"Expected Result: {expected_outputs[idx]}. Actual Result: {result}")
    print("All example tests passed!")

    import random

    def brute_force(A):
        # Simulate: greedily press leftmost off bulb, actually flip array.
        A = A[:]
        n = len(A)
        presses = 0
        for i in range(n):
            if A[i] == 0:
                presses += 1
                for j in range(i, n):
                    A[j] = 1 - A[j]
        return presses

    for trial in range(300):
        n = random.randint(0, 12)
        A = [random.randint(0, 1) for _ in range(n)]
        got = bulbs(A[:])
        expected = brute_force(A[:])
        assert got == expected, f"Mismatch on {A}: got {got}, expected {expected}"

    print("All stress tests passed!")
