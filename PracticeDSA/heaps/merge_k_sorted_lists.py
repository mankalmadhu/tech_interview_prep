# https://leetcode.com/problems/merge-k-sorted-lists/
"""
Merge K Sorted Lists

You're given an array of k linked lists, each sorted in ascending
order. Merge all the lists into one sorted linked list and return
its head.

Approach: min-heap based k-way merge.
1. Push the head node of each of the k lists onto a min-heap (at
   most k elements in the heap at any time - one "current candidate"
   per list, not all N nodes across all lists).
2. Repeat: pop the min node from the heap - this becomes the next
   node in the merged result. If that popped node has a `.next`,
   push `.next` onto the heap (replacing that list's candidate slot).
3. Continue until the heap is empty.

Edge case: a list entry can legitimately be None (an empty sub-list),
or the whole `lists` array can be empty - these aren't malformed
input, LeetCode explicitly allows them. Each None entry should simply
be skipped when seeding the heap, not treated as a reason to bail out
of the whole function.

Gotcha: heapq compares tuples element-wise. If you push (val, node)
and two nodes have the SAME val, heapq will try to compare the
ListNode objects themselves as a tiebreaker - but ListNode doesn't
support comparison (<), so this crashes. Push a tiebreaker in the
middle: (val, unique_counter, node), where unique_counter is a
strictly increasing int that's always different across all pushes,
guaranteeing heapq never needs to compare the node objects
themselves.

Complexity Analysis:
--------------------
Time:  O(N log K), where N = total number of nodes across all k
       lists, K = number of lists. Each node is pushed and popped
       exactly once; the heap never holds more than K elements, so
       each push/pop costs O(log K).
Space: O(K) for the heap (at most one candidate per list at any
       time).
"""

import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(lists):
    heap = []
    count = 0

    for li in lists:
        if li is None:
            continue
        count += 1
        heapq.heappush(heap, (li.val, count, li))

    result = []
    while heap:
        cur_min = heapq.heappop(heap)
        result.append(cur_min[0])
        if cur_min[2].next:
            count += 1
            heapq.heappush(heap, (cur_min[2].next.val, count, cur_min[2].next))

    return build_list(result)


def build_list(values):
    """Helper: build a linked list from a Python list, return head."""
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head):
    """Helper: convert a linked list back into a Python list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    lists1 = [build_list([1, 4, 5]), build_list([1, 3, 4]), build_list([2, 6])]
    assert to_list(solve(lists1)) == [1, 1, 2, 3, 4, 4, 5, 6]

    assert solve([]) is None
    assert solve([build_list([])]) is None

    print("Example tests passed!")

    # ---- stress test vs independent brute force ----
    import random

    def brute_force(values_per_list):
        """Independent reference: flattens all values and sorts with
        Python's built-in sort, no heap/merge logic shared with the
        real solution."""
        merged = []
        for values in values_per_list:
            merged.extend(values)
        return sorted(merged)

    random.seed(42)
    trials = 300
    for t in range(trials):
        num_lists = random.randint(0, 6)
        values_per_list = []
        for _ in range(num_lists):
            length = random.randint(0, 6)
            values = sorted(random.randint(-20, 20) for _ in range(length))
            values_per_list.append(values)

        expected = brute_force(values_per_list)
        lists = [build_list(v) for v in values_per_list]
        actual = to_list(solve(lists))

        assert expected == actual, (
            f"mismatch on trial {t}: values_per_list={values_per_list}\n"
            f"expected={expected}, actual={actual}"
        )

    print(f"Stress test passed: {trials} trials.")
