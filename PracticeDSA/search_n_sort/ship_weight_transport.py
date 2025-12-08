class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        """
        Calculates the minimum ship capacity required to transport all packages within B days.

        Strategy: Binary Search on Answer
        ---------------------------------
        Instead of searching the array 'A', we search for the *capacity* itself.
        
        1. Search Space Definition:
           - Lower Bound (low): max(A). The ship MUST be large enough to carry 
             the single heaviest package.
           - Upper Bound (high): sum(A). In the worst case (1 day), the ship 
             must carry everything at once.
        
        2. The Search (Minimization):
           - We pick a candidate capacity 'mid'.
           - We run a greedy check (`canShipWeight`) to see if it's possible 
             to ship all packages within 'B' days using this capacity.
           - If Possible (True): We record this as a potential answer and try 
             to find a *smaller* valid capacity (move high to left).
           - If Not Possible (False): We need a *larger* capacity (move low to right).

        Complexity Analysis:
        --------------------
        Time Complexity: O(N * log(Sum(A) - Max(A)))
           - The Binary Search runs on the range of possible capacities (S). 
             The number of iterations is O(log S).
           - Inside each iteration, `canShipWeight` iterates through the array 'A' 
             once to simulate the shipping. This takes O(N).
           - Total = O(N * log S).

        Space Complexity: O(1)
           - We only use a few variables for pointers and sums. We do not use 
             extra data structures proportional to the input size.

        Example Trace:
        --------------
        Input: A = [1, 2, 3], B = 2
        Range: [max(3), sum(6)] -> [3, 6]

        1. Iteration 1:
           - mid = (3 + 6) // 2 = 4
           - check(4): 
             - Day 1: Load 1, Load 2. (Current Load: 3). Next is 3 (3+3 > 4), so stop.
             - Day 2: Load 3. (Current Load: 3).
             - Success! Valid in 2 days.
           - Update: globalMin = 4. Try smaller: high = 3.

        2. Iteration 2:
           - Range: [3, 3]. mid = 3.
           - check(3):
             - Day 1: Load 1, Load 2. (Load: 3). Full.
             - Day 2: Load 3. (Load: 3). Full.
             - Success! Valid in 2 days.
           - Update: globalMin = 3. Try smaller: high = 2.

        3. Stop: low (3) > high (2). Return 3.
        """
        low = max(A)
        high = sum(A)
        global_min = high  # Initialize with the worst-case capability

        while low <= high:
            mid = (low + high) // 2
            if self.can_ship_weight(A, B, mid):
                global_min = mid
                high = mid - 1
            else:
                low = mid + 1

        return global_min

    def can_ship_weight(self, A, B, capacity):
        days = 1
        cur_load = 0

        for weight in A:
            if weight + cur_load > capacity:
                # once the days is incremented the previous cur_load is not used and cur_load is init to cur weight
                days += 1
                cur_load = weight
            else:
                cur_load += weight
        
        return days <= B