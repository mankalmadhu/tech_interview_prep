"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/arrays/top_k_frequent.py until you're done.

Problem (Top K Frequent Elements, LeetCode 347):

Given an integer array nums and an integer k, return the k most
frequent elements. You may return the answer in any order.

Example:
  nums = [1,1,1,2,2,3], k = 2
  output = [1,2]

Write your solution below.
"""

from collections import Counter


def top_k_frequent(nums, k):
    lookup = Counter(nums)

    bucket = [[] for _ in range(len(nums)+1)]

    for num, freq in lookup.items():
        bucket[freq].append(num)

    result = []
    for i in range(len(bucket)-1,0, -1):
        for n in bucket[i]:
            result.append(n)
            if len(result) == k:
                return result


if __name__ == "__main__":
    print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))  # expect [1, 2] (order may vary)
    print(top_k_frequent([1], 1))  # expect [1]

    assert set(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == {1, 2}
    assert set(top_k_frequent([1], 1)) == {1}
    assert set(top_k_frequent([1, 2], 2)) == {1, 2}
    assert top_k_frequent([4, 1, 1, 1, 2, 2, 3], 1) == [1]
    print("fixed cases passed")

    import random

    def brute_force(nums, k):
        counts = Counter(nums)
        ranked = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)
        return [num for num, _ in ranked[:k]]

    for _ in range(300):
        n = random.randint(1, 30)
        nums = [random.randint(1, 8) for _ in range(n)]
        k = random.randint(1, len(set(nums)))
        got = top_k_frequent(nums, k)
        want = brute_force(nums, k)

        counts = Counter(nums)
        got_freqs = sorted((counts[x] for x in got), reverse=True)
        want_freqs = sorted((counts[x] for x in want), reverse=True)
        assert len(got) == k, f"nums={nums}, k={k}: expected {k} elements, got {got}"
        assert got_freqs == want_freqs, (
            f"nums={nums}, k={k}: got {got} (freqs {got_freqs}), "
            f"want {want} (freqs {want_freqs})"
        )
    print("300 randomized trials passed")
