# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        i = k - 1
        check = head
        while check and i:
            check = check.next
            i -= 1
        #end = self.move(head, k)
        #print(f"end: {end.val if end else None}")
        if not check:
            return head
        
        #reverse list
        newtail = head
        curr = head
        prev = None
        i = k
        while curr and i:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
            i -= 1
        rest = self.reverseKGroup(curr, k)
        newtail.next = rest
        return prev

    
    def move(self, From: Optional[ListNode], by: int) -> Optional[ListNode]:
        i = by
        while From and i:
            From = From.next
            i -= 1
        return From