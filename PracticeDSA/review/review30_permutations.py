"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/backtrack/permutations.py until you're done.

Problem (Permutations, LeetCode 46):

Given an array `nums` of distinct integers, return all possible
permutations (in any order).

Example:
  nums = [1, 2, 3]
  -> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Write your solution below (backtracking: choose -> explore -> un-choose).
"""


def permute(nums):
    result = []
    used = set()

    backtrack(nums,[], result, used)
    return result

def backtrack(nums, cur_perm, result, used):

    if len(cur_perm) == len(nums):
        result.append(cur_perm[:])
        return result

    for i in range(len(nums)):

        if i in used:
            continue

        cur_perm.append(nums[i])
        used.add(i)

        backtrack(nums, cur_perm,result, used)

        used.remove(i)
        cur_perm.pop()



if __name__ == "__main__":
    def normalize(perms):
        return sorted(tuple(p) for p in perms)

    import itertools

    for nums in [[1, 2, 3], [0, 1], [5], []]:
        got = normalize(permute(nums))
        want = normalize(list(itertools.permutations(nums)))
        assert got == want, f"{nums}: expected {want}, got {got}"
    print("fixed cases passed")
