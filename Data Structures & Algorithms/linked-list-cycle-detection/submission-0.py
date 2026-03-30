# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodeHash = {}
        while head:
            if head in nodeHash:
                return True
            else:
                nodeHash[head] = True
            head = head.next
        return False
        