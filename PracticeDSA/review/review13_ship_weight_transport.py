"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/search_n_sort/ship_weight_transport.py until you're done.

Problem (Capacity To Ship Packages Within D Days, LeetCode 1011):

You have an array A of package weights that must be shipped, in order,
within B days. Each day, you load consecutive packages onto the ship
(in the same order as A) up to the ship's weight capacity, without
exceeding it (a single package's weight never exceeds the capacity).

Find the LEAST ship capacity such that all packages can be shipped
within B days.

Example:
  A = [1, 2, 3], B = 2 -> answer: 3
    (Day 1: ship 1+2=3, Day 2: ship 3)

  A = [3, 2, 2, 4, 1, 4], B = 3 -> answer: 6

Write your solution below.
"""


class Solution:
    def solve(self, A, B):
        high = sum(A)
        low = max(A)

        min_ship_weight = high

        while low <= high:
            mid = (low + high)//2

            if self.can_ship_weight(mid, A, B):
                high = mid -1
                min_ship_weight = mid
            else:
                low = mid + 1

        return min_ship_weight

    def can_ship_weight(self,capacity, A, B):
        days = 1
        cur_weight = 0

        for w in A:
            if (cur_weight + w) <= capacity:
                cur_weight += w
            else:
                cur_weight = w
                days += 1

        return days <=B


if __name__ == "__main__":
    # add your own test calls here once implemented
    s= Solution()
    A = [1, 2, 3]
    B = 2
    print(s.solve(A,B))
