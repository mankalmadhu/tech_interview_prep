from typing import List

class Solution:
    """
    Merges overlapping intervals in an array.
    
    Time Complexity: O(N log N) dominated by the initial sorting operation.
    Space Complexity: O(1) auxiliary space, O(N) to store the merged_list output.
    
    The Logic:
    - Sort the intervals based on their starting value. This guarantees that any
      potential overlap must happen with the very last interval we processed.
    - Initialize `merged_list` with the first interval.
    - Iterate through the rest. If the current interval's start is <= the previous 
      interval's end, they overlap!
    - Merge them safely by stretching the previous interval's end to the max of both ends.
    - If they don't overlap, simply append the current interval to the list.
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged_list = []

        if not intervals:
            return merged_list
        
        intervals.sort(key=lambda x: x[0])    
        merged_list.append(intervals[0])

        for i in range(1,len(intervals)):
            cur_start, cur_end = intervals[i]
            prev_start, prev_end = merged_list[-1]
            
            if cur_start <= prev_end:
                merged_list[-1][1] = max(prev_end, cur_end)
            else:
                merged_list.append(intervals[i])
        
        return merged_list

if __name__ == '__main__':
    sol = Solution()
    print("Test 1: [[1,3],[2,6],[8,10],[15,18]] -> Expected: [[1, 6], [8, 10], [15, 18]], Got:", sol.merge([[1,3],[2,6],[8,10],[15,18]]))
    print("Test 2: [[1,4],[4,5]]                -> Expected: [[1, 5]],                   Got:", sol.merge([[1,4],[4,5]]))
    print("Test 3: [[1,4],[2,3]]                -> Expected: [[1, 4]],                   Got:", sol.merge([[1,4],[2,3]]))
    print("All tests executed!")
