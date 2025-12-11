class Solution:
  # @param A : list of integers
  # @return an integer
  # https://www.interviewbit.com/problems/bulbs/
  def bulbs(self, A):
    """
    Calculates the minimum number of switches to turn all bulbs ON.

    Problem Context:
    ----------------
    - N bulbs are in a row.
    - Turning on a switch at index 'i' flips the state of ALL bulbs from i to N-1.
    - Goal: Find minimum switches to reach a state where all bulbs are ON (1).

    Strategy: Greedy Approach with State Tracking
    ---------------------------------------------
    We iterate through the bulbs from left to right.
    The state of the current bulb A[i] is determined by:
      1. Its original value.
      2. The number of times we have flipped switches previously (count).
    
    Logic:
    - If 'count' is EVEN: The bulb is in its original state A[i].
    - If 'count' is ODD: The bulb is in the toggled state (1 - A[i]).
    
    If the effective state is 0 (OFF), we MUST flip the switch at this position 
    to turn it ON. This increments 'count' and affects all future bulbs.

    Complexity Analysis:
    --------------------
    Time Complexity: O(N)
       - We traverse the list exactly once.
    Space Complexity: O(1)
       - We only use a single variable 'count' to track the state.

    Example Trace:
    --------------
    Input: [0, 1, 0, 1]
    
    1. i=0, Val=0. Count=0 (Even).
       - Effective State: 0 (OFF).
       - Action: FLIP switch. Count becomes 1.
    
    2. i=1, Val=1. Count=1 (Odd).
       - Effective State: 1 flipped is 0 (OFF).
       - Action: FLIP switch. Count becomes 2.

    3. i=2, Val=0. Count=2 (Even).
       - Effective State: 0 (OFF).
       - Action: FLIP switch. Count becomes 3.

    4. i=3, Val=1. Count=3 (Odd).
       - Effective State: 1 flipped is 0 (OFF).
       - Action: FLIP switch. Count becomes 4.

    Result: 4 switches.
    """
    count = 0
    for i in range(len(A)):

      effective_value = A[i] if count % 2 == 0 else 1 - A[i]

      if effective_value == 0:
        count += 1

    return count


# [ 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1 ]
# [ 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
# [ 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1]
# [ 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
# [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

if __name__ == "__main__":
  sol = Solution()
  A = [1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1]
  print(sol.bulbs(A))
