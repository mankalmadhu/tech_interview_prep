"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/linked_list/linked_list_cycle.py until you're done.

Problem (Linked List Cycle, LeetCode 141):

Given the head of a linked list, determine if the linked list has a
cycle in it (some node's `next` pointer loops back to an earlier node).

Example:
  3 -> 2 -> 0 -> -4 -> (back to node 2)  -> True
  1 -> 2 -> None                         -> False

Write your solution below (Floyd's Tortoise and Hare, O(N) time, O(1) space).
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head):

        fastPtr = head
        slowPtr = head

        if head == None or head.next == None:
            return False

        while fastPtr != None and fastPtr.next != None:
            fastPtr = fastPtr.next.next
            slowPtr = slowPtr.next

            if fastPtr == slowPtr:
                return True

        return False


if __name__ == "__main__":
    sol = Solution()

    # cycle: 3 -> 2 -> 0 -> -4 -> back to node(2)
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(-4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2
    assert sol.hasCycle(n1) is True

    # no cycle
    m1 = ListNode(1)
    m2 = ListNode(2)
    m1.next = m2
    assert sol.hasCycle(m1) is False

    # single node, no cycle
    assert sol.hasCycle(ListNode(1)) is False

    # single node, self-cycle
    s1 = ListNode(1)
    s1.next = s1
    assert sol.hasCycle(s1) is True

    # empty list
    assert sol.hasCycle(None) is False

    print("fixed cases passed")
