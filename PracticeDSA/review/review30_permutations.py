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

def permute_iterative(nums):
    result = [[]]

    for num in nums:
        cur_perm = []
        for r in result:
            for i in range(len(r)+1):
                cur_perm.append(r[:i] + [num] + r[i:])
            result = cur_perm

    return result






if __name__ == "__main__":
    def normalize(perms):
        return sorted(tuple(p) for p in perms)

    import itertools

    for nums in [[1, 2, 3], [0, 1], [5], []]:
        got = normalize(permute(nums))
        print(f"got:{got}")
        want = normalize(list(itertools.permutations(nums)))
        assert got == want, f"{nums}: expected {want}, got {got}"
    print("fixed cases passed")

    for nums in [[1, 2, 3], [0, 1], [5], []]:
        got_it = normalize(permute_iterative(nums))
        want = normalize(list(itertools.permutations(nums)))
        assert got_it == want, f"iterative {nums}: expected {want}, got {got_it}"
    print("iterative fixed cases passed")

    import random
    for _ in range(300):
        n = random.randint(0, 6)
        nums = random.sample(range(0, 20), n)
        got = normalize(permute(nums))
        got_it = normalize(permute_iterative(nums))
        want = normalize(list(itertools.permutations(nums)))
        assert got == want
        assert got_it == want
    print("300 randomized trials passed (backtracking + iterative)")

    print(permute_iterative([0,1]))
