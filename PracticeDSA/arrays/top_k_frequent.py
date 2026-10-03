from typing import List
import heapq


class Solution:
    """
    Finds the top k most frequent elements in an array.

    Approach 1: Min-Heap (topKFrequent)
    - Time Complexity: O(N + U log k) where U is the number of unique elements.
    - Space Complexity: O(U + k) -> O(U) for the frequency dictionary and heap.

    Approach 2: Bucket Sort (topKFrequentBucket)
    - Time Complexity: O(N) because we efficiently map frequencies to array indices.
    - Space Complexity: O(N) to store the buckets array and frequency dictionary.
    """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_counter = {}
        for num in nums:
            freq_counter[num] = freq_counter.get(num, 0) + 1

        heap = []
        for num, freq in freq_counter.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [item[1] for item in heap]

    def topKFrequentBucket(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]

        freq_counter = {}
        for num in nums:
            freq_counter[num] = freq_counter.get(num, 0) + 1

        for num, freq in freq_counter.items():
            bucket[freq].append(num)

        result = []
        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                result.append(n)
                if len(result) == k:
                    return result


if __name__ == "__main__":
    sol = Solution()
    print("Heap Approach:")
    print(
        "Test 1: nums=[1,1,1,2,2,3], k=2 -> Expected: [1, 2], Got:",
        sol.topKFrequent([1, 1, 1, 2, 2, 3], 2),
    )
    print(
        "Test 2: nums=[1], k=1           -> Expected: [1],    Got:",
        sol.topKFrequent([1], 1),
    )

    print("\nBucket Sort Approach:")
    print(
        "Test 1: nums=[1,1,1,2,2,3], k=2 -> Expected: [1, 2], Got:",
        sol.topKFrequentBucket([1, 1, 1, 2, 2, 3], 2),
    )
    print(
        "Test 2: nums=[1], k=1           -> Expected: [1],    Got:",
        sol.topKFrequentBucket([1], 1),
    )
    print("All tests executed!")

    assert set(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2)) == {1, 2}
    assert set(sol.topKFrequentBucket([1, 1, 1, 2, 2, 3], 2)) == {1, 2}
    assert set(sol.topKFrequent([1], 1)) == {1}
    assert set(sol.topKFrequentBucket([1], 1)) == {1}
    assert sol.topKFrequentBucket([4, 1, 1, 1, 2, 2, 3], 1) == [1]
    print("fixed cases passed")

    import random
    from collections import Counter

    def brute_force(nums, k):
        counts = Counter(nums)
        ranked = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)
        return [num for num, _ in ranked[:k]]

    for _ in range(300):
        n = random.randint(1, 30)
        nums = [random.randint(1, 8) for _ in range(n)]
        k = random.randint(1, len(set(nums)))
        want = brute_force(nums, k)
        want_freqs = sorted((Counter(nums)[x] for x in want), reverse=True)

        for fn in (sol.topKFrequent, sol.topKFrequentBucket):
            got = fn(nums, k)
            got_freqs = sorted((Counter(nums)[x] for x in got), reverse=True)
            assert len(got) == k, f"{fn.__name__}: nums={nums}, k={k}, got {got}"
            assert got_freqs == want_freqs, (
                f"{fn.__name__}: nums={nums}, k={k}: got {got} (freqs {got_freqs}), "
                f"want {want} (freqs {want_freqs})"
            )
    print("300 randomized trials passed (both approaches)")
