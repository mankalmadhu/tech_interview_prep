from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Determines if a linked list contains a cycle using Floyd's Cycle-Finding Algorithm.
        Time Complexity: O(N) | Space Complexity: O(1)
        
        The Logic (Tortoise and Hare):
        - `fastPtr` moves 2 steps at a time, `slowPtr` moves 1 step at a time.
        - If there is a cycle, `fastPtr` will eventually lap and meet `slowPtr`.
        - If `fastPtr` or `fastPtr.next` reaches None, the list has a finite end (no cycle).
        
        Note: The node where they meet is inside the cycle, but NOT necessarily the start.
        To find the EXACT start of the cycle (Phase 2 of Floyd's Algorithm):
        1. Leave `fastPtr` at the collision point.
        2. Move `slowPtr` back to `head`.
        3. Advance both pointers 1 step at a time.
        4. The node where they collide again is mathematically guaranteed to be the start!
        """
        fastPtr = head
        slowPtr = head

        if(head ==None or head.next == None):
            return False
        
        while(fastPtr !=None and fastPtr.next != None):
            fastPtr = fastPtr.next.next
            slowPtr = slowPtr.next

            if(fastPtr == slowPtr):
                return True
        
        return False
