def permute(nums):
    """
    Generates all possible permutations of a given list of numbers.

    This function uses a backtracking approach to explore every possible
    ordering of the numbers from the input list.

    Args:
        nums: A list of unique integers.

    Returns:
        A list of lists, where each inner list is a unique permutation of `nums`.

    Trace for nums = [1, 2, 3]:
        The process starts with an initial call to `backtrack(current_permutation=[], used=set())`.

        1. The loop in `backtrack` tries to pick the first number. Let's say it picks `1`.
           - CHOOSE: `current_permutation` becomes `[1]`, `used` becomes `{0}`.
           - EXPLORE: A recursive call is made: `backtrack([1], {0})`.

        2. Inside this new call, the loop tries to pick the second number.
           - It skips `1` because its index `0` is in the `used` set.
           - It picks `2`.
           - CHOOSE: `current_permutation` becomes `[1, 2]`, `used` becomes `{0, 1}`.
           - EXPLORE: A recursive call is made: `backtrack([1, 2], {0, 1})`.

        3. Inside this third call, the loop tries to pick the third number.
           - It skips `1` and `2`. It picks `3`.
           - CHOOSE: `current_permutation` becomes `[1, 2, 3]`.
           - EXPLORE: `backtrack([1, 2, 3], {0, 1, 2})`.

        4. BASE CASE: The length is now 3. `[1, 2, 3]` is added to the results.
           The function returns.

        5. UN-CHOOSE (Backtrack): The state is rewound.
           - `3` is popped from the permutation, `2` is removed from `used`.
           - `current_permutation` is `[1, 2]` again. The loop in this call is over. It returns.

        6. UN-CHOOSE (Backtrack): The state is rewound again.
           - `2` is popped from the permutation, `1` is removed from `used`.
           - `current_permutation` is `[1]` again.

        7. The loop from step 2 continues. It now picks `3` as the second number,
           starting the process to find the permutation `[1, 3, 2]`.

        This entire process repeats, starting from step 1, by picking `2` and then `3`
        as the initial numbers, until all N! permutations are found.

        Algorithm: Backtracking (Choose -> Explore -> Un-choose)
        - Time Complexity: O(N * N!). There are N! permutations. For each permutation, 
          it takes O(N) time to copy the path (`cur[:]`) into the result list.
        - Space Complexity: O(N) for the recursion stack and the `cur` path, plus O(N) 
          for the `used` set. (Excluding the O(N * N!) space used to hold the final output).

        Note for Next Review:
        - Be prepared to discuss the exact mathematical derivation of the O(N * N!) time complexity.

    """
    result = []
    used = set()
    backtrack([], used, result, nums)
    return result


def backtrack(current_permutation, used, result, nums):
    if len(current_permutation) == len(nums):
        result.append(current_permutation[:])
        return

    for i in range(len(nums)):
        if i in used:
            continue

        # Choose
        current_permutation.append(nums[i])
        used.add(i)
        
        # Explore
        backtrack(current_permutation, used, result, nums)
        
        # Un-choose (Backtrack)
        used.remove(i)
        current_permutation.pop()