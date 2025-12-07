def build_powerset(nums):
    """
    Generates all possible subsets (the power set) of a given list of numbers.

    This function uses a backtracking approach to explore every possible
    combination of including or excluding each number from the input list.

    Args:
        nums: A list of unique integers.

    Returns:
        A list of lists, where each inner list is a unique subset of `nums`.

    Trace for nums = [1, 2, 3]:
        The process starts with an initial call to `backtrack(index=0, current_subset=[])`.

        1. backtrack(0, []): Considers the number `1`.
           - Path 1 (Exclude 1): Calls `backtrack(1, [])`.
             - backtrack(1, []): Considers the number `2`.
               - Path 1.1 (Exclude 2): Calls `backtrack(2, [])`.
                 - backtrack(2, []): Considers the number `3`.
                   - Path 1.1.1 (Exclude 3): Calls `backtrack(3, [])`.
                     -> Base Case: index is 3. Add a copy of `[]` to results.
                   - Path 1.1.2 (Include 3):
                     -> current_subset becomes [3].
                     -> Calls `backtrack(3, [3])`. Base Case. Add `[3]` to results.
                     -> Backtrack: pop `3`. current_subset is `[]` again.
               - Path 1.2 (Include 2):
                 -> current_subset becomes [2].
                 -> Calls `backtrack(2, [2])`. This will generate `[2]` and `[2, 3]`.
                 -> Backtrack: pop `2`. current_subset is `[]` again.
           - Path 2 (Include 1):
             -> current_subset becomes [1].
             -> Calls `backtrack(1, [1])`. This will explore all paths starting
                with `1`, generating `[1]`, `[1, 3]`, `[1, 2]`, and `[1, 2, 3]`.
             -> Backtrack: pop `1`. current_subset is `[]` again.
        
        The final result is the collection of all subsets found at the base cases.
    """
    result = []
    # Using a helper to avoid making 'result' a default mutable argument
    backtrack(0, [], nums, result)
    return result

def backtrack(index, current_subset, nums, results):
    # Base case: if we've considered all numbers
    if index >= len(nums):
        # Add a copy of the current subset to the results
        results.append(current_subset[:])
        return
    
    # --- Decision 1: Exclude the current number ---
    # Don't add nums[index] to the current_subset
    backtrack(index + 1, current_subset, nums, results)

    # --- Decision 2: Include the current number ---
    # Add nums[index] to the current_subset
    current_subset.append(nums[index])
    # Explore further with this new subset
    backtrack(index + 1, current_subset, nums, results)
    # Backtrack: remove the number to clean up for the next recursive calls
    current_subset.pop()