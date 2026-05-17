class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Reverses a singly linked list in-place.
    
    Time Complexity: O(N)
    - We iterate through the N nodes of the linked list exactly once.
    
    Space Complexity: O(1)
    - We strictly use three pointers (prev, cur, next_node) to perform the 
      reversal in-place without allocating any extra data structures.
      
    Logic & Trade-offs:
    - Iterative approach: We maintain a `prev` pointer (initially None) and 
      a `cur` pointer. We temporarily store `cur.next`, flip `cur.next` to 
      point backward at `prev`, and then shift both pointers forward.
    - Recursive approach trade-off: A recursive solution is elegant but forces 
      the system call stack to grow to depth N, resulting in an inefficient 
      O(N) space complexity and potential RecursionError on massive lists.
    """
    def reverseList(self, head: ListNode) -> ListNode:
        
        if not head:
            return head
        prev = None
        cur = head
        while cur != None:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        
        return prev

if __name__ == '__main__':
    def build_list(values):
        if not values: return None
        head = ListNode(values[0])
        curr = head
        for val in values[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        return head

    def get_list_values(head):
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
        return values

    sol = Solution()
    
    # Test 1
    head1 = build_list([1, 2, 3, 4, 5])
    rev1 = sol.reverseList(head1)
    print("Test 1: [1,2,3,4,5] -> Expected: [5, 4, 3, 2, 1], Got:", get_list_values(rev1))

    # Test 2
    head2 = build_list([1, 2])
    rev2 = sol.reverseList(head2)
    print("Test 2: [1,2]       -> Expected: [2, 1], Got:", get_list_values(rev2))

    # Test 3
    head3 = build_list([])
    rev3 = sol.reverseList(head3)
    print("Test 3: []          -> Expected: [], Got:", get_list_values(rev3))

    print("All tests executed!")

