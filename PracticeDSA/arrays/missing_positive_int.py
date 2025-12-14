

class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        """
        Finds the smallest missing positive integer.

        Strategy: Cyclic Sort (Bucketing)
        ---------------------------------
        1. Concept: Ideally, A[i] should hold the value (i + 1).
           - Index 0 holds 1, Index 1 holds 2, etc.
        2. Pass 1 (Place Numbers): Iterate through the array.
           - While the current number A[i] is in the valid range [1, N] AND 
             it is NOT in its correct position (index A[i]-1):
             - Swap A[i] with the number at its correct position.
             - This places A[i] in its "home" bucket.
           - Ignore negative numbers and numbers > N (they can't form the 
             sequence 1..N).
        3. Pass 2 (Find Missing): Iterate through the array again.
           - The first index 'i' where A[i] != i + 1 reveals that (i + 1) is 
             missing.
        4. Fallback: If all positions match (e.g., [1, 2, 3]), the missing 
           number is N + 1.

        Complexity Analysis:
        --------------------
        Time Complexity: O(N)
           - Each number is swapped at most once into its correct position.
        Space Complexity: O(1)
           - In-place modification of the array.

        Example Trace:
        --------------
        Input: [3, 4, -1, 1]
        
        1. i=0, Val=3. Correct Pos is index 2.
           - Swap 3 and A[2] (-1).
           - Array: [-1, 4, 3, 1]
           - Current Val is -1 (Ignore/Next).

        2. i=1, Val=4. Correct Pos is index 3.
           - Swap 4 and A[3] (1).
           - Array: [-1, 1, 3, 4]
           - Current Val is 1. Correct Pos is index 0.
           - Swap 1 and A[0] (-1).
           - Array: [1, -1, 3, 4]
           - Current Val is -1 (Ignore/Next).

        3. i=2, Val=3. Correct Pos is index 2. (Already there). Next.
        4. i=3, Val=4. Correct Pos is index 3. (Already there). Next.

        Final Check:
        - Index 0: Val 1 == 1 (OK)
        - Index 1: Val -1 != 2 (MISMATCH!) -> Return 2.
        """
        n = len(A)
    
        i = 0
        while i < n:
            correct_pos = A[i] - 1
            if 1 <= A[i] <= n and A[i] != A[correct_pos]:
                A[i], A[correct_pos] = A[correct_pos], A[i]
            else:
                i += 1
    
        for i in range(n):
            if A[i] != i + 1:
                return i + 1
    
        return n + 1


def main():

    inputs = [[1, 2, 0], [3, 4, -1, 1], [1, 2, 3], [1, 2, 3, 4, 5, 6, 7],
              [-8, -7, -6]]
    expected_outputs = [3, 2, 4, 8, 1]
    for idx, A in enumerate(inputs):
        sol = Solution()
        result = sol.firstMissingPositive(A)
        print(
            f"Expected Result: {expected_outputs[idx]}.Actual Result:{result}")
