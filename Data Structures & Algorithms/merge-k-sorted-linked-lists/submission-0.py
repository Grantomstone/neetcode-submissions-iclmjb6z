import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        heap = []
        for li in lists:
            curr = li
            while curr:
                heapq.heappush(heap, curr.val)
                curr = curr.next
        
        if len(heap) == 0:
            return None
        head = ListNode(val=heapq.heappop(heap))
        curr = head
        while heap:
            new = ListNode(val=heapq.heappop(heap))
            curr.next = new
            curr = new
        return head
