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

if __name__ == '__main__':
    sol = Solution()
    print("Heap Approach:")
    print("Test 1: nums=[1,1,1,2,2,3], k=2 -> Expected: [1, 2], Got:", sol.topKFrequent([1,1,1,2,2,3], 2))
    print("Test 2: nums=[1], k=1           -> Expected: [1],    Got:", sol.topKFrequent([1], 1))
    
    print("\nBucket Sort Approach:")
    print("Test 1: nums=[1,1,1,2,2,3], k=2 -> Expected: [1, 2], Got:", sol.topKFrequentBucket([1,1,1,2,2,3], 2))
    print("Test 2: nums=[1], k=1           -> Expected: [1],    Got:", sol.topKFrequentBucket([1], 1))
    print("All tests executed!")
