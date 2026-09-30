"""
Review scratchpad — solve from scratch, do NOT peek at
PracticeDSA/linked_list/reverse_linked_list.py until you're done.

Problem (Reverse Linked List, LeetCode 206):

Given the head of a singly linked list, reverse the list in-place and
return the new head.

Example:
  [1,2,3,4,5] -> [5,4,3,2,1]
  [1,2]       -> [2,1]
  []          -> []

Write your solution below (iterative, three-pointer approach).
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        if not head:
            return

        cur = head
        prev = None
        while cur != None:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        return prev


if __name__ == "__main__":
    # add your own test calls here once implemented
    pass
