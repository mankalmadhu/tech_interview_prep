"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/strings/salutes.py until you're done (it's currently
broken/unparseable anyway).

Problem: A string A consists of '>' (person walking right) and
'<' (person walking left) in a hallway. Whenever two people cross
paths, they salute each other. Return the total number of salutes.

Given examples to calibrate against (figure out the convention
yourself — don't assume, derive it from these):
  A = ">>><<<"  -> 9
  A = "<>"      -> 0

Write your solution below.
"""


class Solution:
    def countSalutes(self, A):
        rightCount = 0
        totalSalutes = 0

        for salute in A:
            if salute == '>':
                rightCount +=1
            else:
                totalSalutes += rightCount

        return totalSalutes


if __name__ == "__main__":
    sol = Solution()
    # add your own test calls here once implemented
