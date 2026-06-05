# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        temp = head
        while temp:
            temp = temp.next
            length += 1
        
        target = length - n
        if target == 0:
            return head.next
        
        i = 1
        nu = head
        while i < target:
            nu = nu.next
            i += 1
        pre = nu
        if nu.next == None:
            pre.next = None
            return head
        else:
            post = nu.next.next
            pre.next = post
            return head
            
        