#https://www.interviewbit.com/problems/kth-smallest-element-in-the-array/
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        """
        Finds the B-th smallest element in the array.

        Strategy: Binary Search on Answer (Value Range)
        -----------------------------------------------
        Instead of sorting the array (which takes O(N log N)), we search the 
        range of possible values [min(A), max(A)].

        1. Range Definition:
           - Low = min(A), High = max(A).
        
        2. The Search Loop:
           - Pick a candidate value 'mid'.
           - Count how many numbers in A are less than or equal to 'mid'.
           - Decision:
             - If count < B: 'mid' is too small. We need more numbers. 
               Move low to mid + 1.
             - If count >= B: 'mid' is large enough to cover the B-th rank. 
               It could be the answer, or the answer is smaller. 
               Move high to mid (keep mid as a candidate).

        Complexity Analysis:
        --------------------
        Time Complexity: O(N * log(max(A) - min(A)))
           - The search space is the range of values (R). Binary search takes O(log R).
           - Each step involves a linear scan of A, taking O(N).
        
        Space Complexity: O(1)
           - No auxiliary data structures used.

        Example Trace (A = [2, 1, 4, 3, 2], B = 3):
        -------------------------------------------
        Target: We want the 3rd smallest element. 
        (Sorted A would be [1, 2, 2, 3, 4], so answer should be 2).
        Initial: low = 1, high = 4.

        Iter 1: 
          mid = (1 + 4) // 2 = 2
          Count numbers in A <= 2: [2, 1, 2] -> count is 3.
          Since count (3) >= B (3), it means the 3rd smallest is <= 2.
          Move high to mid -> high = 2.

        Iter 2:
          low = 1, high = 2
          mid = (1 + 2) // 2 = 1
          Count numbers in A <= 1: [1] -> count is 1.
          Since count (1) < B (3), 'mid' is too small. 3rd smallest must be > 1.
          Move low to mid + 1 -> low = 2.

        Iter 3:
          low = 2, high = 2. Loop breaks.
          Return low (2).
        """
        low = min(A)
        high = max(A)
        while low < high:
            mid = (low+high)//2
            count = 0
            for num in A:
                if num <= mid:
                    count += 1
            if count < B:
                low = mid+1
            else:
                high = mid
        
        return low

class QuickSelectSolution:
    def kthsmallest(self, A: list[int], B: int) -> int:
        """
        Finds the B-th smallest element using QuickSelect.
        (Note: QuickSelect modifies the array in-place)

        Strategy: Partition and Recurse
        -------------------------------
        1. Pick a pivot (e.g., the last element in the current range).
        2. Partition the array so all elements smaller than pivot are on the left.
        3. The pivot is now at its final absolute sorted position (pivot_idx).
        4. Calculate the relative 'rank' of the pivot within the current sub-array.
           rank = pivot_idx - left + 1
        5. Decision:
           - If rank == k: We found the exact element! Return it.
           - If k < rank: The element is in the left partition. Recurse left.
           - If k > rank: The element is in the right partition. Recurse right,
             but since we skip the left partition, subtract 'rank' from 'k'.

        Complexity Analysis:
        --------------------
        Time Complexity: O(N) Average, O(N^2) Worst-case.
        Space Complexity: O(log N) Average recursion stack, O(N) Worst-case.

        Example Trace (A = [3, 1, 2], B = 1):
        -------------------------------------
        Initial: left=0, right=2, k=1.

        1. partition(A, 0, 2):
           - pivot = A[2] = 2. 
           - i (boundary for smaller elements) starts at -1.
           - Loop j from 0 to 1:
             - j=0: A[0]=3 (Not <= 2).
             - j=1: A[1]=1 (<= 2). Increment i=0. Swap A[i] and A[j]. A -> [1, 3, 2].
           - Loop ends. Swap A[i+1] (A[1]) with pivot (A[right]). A -> [1, 2, 3].
           - Pivot is now at index 1. Return pivot_idx = 1.

        2. quickselect decision:
           - pivot_idx = 1
           - rank of pivot in current sub-array = 1 - 0 + 1 = 2. (Pivot is 2nd smallest).
           - We want k=1. 1 < 2, so the element is in the left partition.
           - Recurse left: quickselect(A, left=0, right=0, k=1).

        3. quickselect(A, 0, 0, 1):
           - left == right, we've converged!
           - Return A[0], which is 1.
        """
        return self.quickselect(A, 0, len(A)-1, B)

    def partition(self, A: list[int], left: int, right: int) -> int:
        pivot = A[right]
        i = left - 1

        for j in range(left, right):
            if A[j] <= pivot:
                i += 1
                A[i], A[j] = A[j], A[i]

        A[i+1], A[right] = A[right], A[i+1]
        return i + 1
    
    def quickselect(self, A: list[int], left: int, right: int, k: int) -> int:
        if left == right:
            return A[left]
        
        pivot_idx = self.partition(A, left, right)
        
        # Calculate rank relative to the current sub-array
        rank = pivot_idx - left + 1

        if k == rank:
            return A[pivot_idx]
        elif k < rank:
            return self.quickselect(A, left, pivot_idx - 1, k)
        else:
            return self.quickselect(A, pivot_idx + 1, right, k - rank)
