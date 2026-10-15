# https://leetcode.com/problems/find-median-from-data-stream/
"""
Find Median from Data Stream

Design a data structure that supports:
- addNum(num): adds an integer from the data stream.
- findMedian(): returns the median of all elements added so far.

Approach: two-heap design.
- A min-heap ("min_heap") holds the larger ("upper") half of the
  numbers seen so far; a max-heap ("max_heap") holds the smaller
  ("lower") half. Python's heapq is min-heap only, so the lower-half
  max-heap is simulated by negating values on push (and negating
  again on read).
- Invariant: the two heap sizes always differ by at most 1. After
  inserting a new number into whichever heap it belongs to (compare
  against the upper heap's current min), rebalance by migrating the
  top element across heaps whenever sizes drift apart by more than
  1.
- findMedian(): if sizes are equal, median = average of (lower
  heap's max, upper heap's min). If one heap has one extra element
  (odd total count), median = that heap's top alone.
- A peek never needs heappop/heappush - heapq always keeps the
  smallest element at index 0 of the underlying list, so heap[0] (or
  -heap[0] for the negated max-heap) is a pure O(1) read.

Complexity Analysis:
--------------------
Time:  addNum - O(log N): one heap push, plus at most one more
       push/pop pair during rebalancing, each O(log N).
       findMedian - O(1): just peeks heap[0] on one or both heaps,
       never pushes/pops.
Space: O(N) - every number ever added stays in one heap or the other
       permanently (never discarded), so total space scales with the
       total count of numbers seen, not log N.
"""

import heapq


class MedianFinder:
    def __init__(self):
        self.min_heap = []  # upper half (larger numbers)
        self.max_heap = []  # lower half (smaller numbers), negated

    def _lower_max(self):
        """Peek the current max of the lower half (max_heap)."""
        return -self.max_heap[0]

    def addNum(self, num):
        if not self.min_heap or num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)

        heap_len_diff = abs(len(self.max_heap) - len(self.min_heap))
        if heap_len_diff > 1:
            if len(self.min_heap) > len(self.max_heap):
                elem = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -elem)
            else:
                elem = heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, -elem)

    def findMedian(self):
        if len(self.min_heap) > len(self.max_heap):
            return float(self.min_heap[0])
        elif len(self.max_heap) > len(self.min_heap):
            return float(self._lower_max())
        else:
            return (self._lower_max() + self.min_heap[0]) / 2


if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    assert mf.findMedian() == 1.5
    mf.addNum(3)
    assert mf.findMedian() == 2

    mf2 = MedianFinder()
    mf2.addNum(-1)
    assert mf2.findMedian() == -1
    mf2.addNum(-2)
    assert mf2.findMedian() == -1.5
    mf2.addNum(-3)
    assert mf2.findMedian() == -2
    mf2.addNum(-4)
    assert mf2.findMedian() == -2.5
    mf2.addNum(-5)
    assert mf2.findMedian() == -3

    print("Example tests passed!")

    # ---- stress test vs independent brute force ----
    import random

    def brute_force_median(nums):
        """Independent reference: re-sorts the full list from scratch
        every time, no heap logic shared with the real solution."""
        s = sorted(nums)
        n = len(s)
        mid = n // 2
        if n % 2 == 1:
            return float(s[mid])
        return (s[mid - 1] + s[mid]) / 2.0

    random.seed(42)
    trials = 300
    for t in range(trials):
        stream_len = random.randint(1, 50)
        stream = [random.randint(-100, 100) for _ in range(stream_len)]

        mf = MedianFinder()
        seen = []
        for num in stream:
            mf.addNum(num)
            seen.append(num)

            expected = brute_force_median(seen)
            actual = mf.findMedian()

            assert expected == actual, (
                f"mismatch on trial {t}: seen so far={seen}\n"
                f"expected={expected}, actual={actual}"
            )

    print(f"Stress test passed: {trials} trials.")
