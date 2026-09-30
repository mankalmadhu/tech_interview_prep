"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/backtrack/powerset.py until you're done.

Problem (Subsets, LeetCode 78):

Given a list of unique integers `nums`, return all possible subsets
(the power set). The solution set must not contain duplicate subsets.

Example:
  nums = [1, 2]    -> [[], [1], [2], [1, 2]]  (order of subsets/elements can vary)
  nums = [1, 2, 3] -> 8 subsets total (2^3)

Write your solution below (backtracking: include/exclude decision at
each index).
"""


def build_powerset(nums):
    result = []
    build_powerset_rec(nums, 0, result, [])
    return result

def build_powerset_rec(nums, index,result, cur_set):
    if index >= len(nums):
        result.append(cur_set[:])
        return

    build_powerset_rec(nums, index+1, result, cur_set)

    cur_set.append(nums[index])
    build_powerset_rec(nums, index+1, result, cur_set)
    cur_set.pop()



if __name__ == "__main__":
    # add your own test calls here once implemented
    pass
