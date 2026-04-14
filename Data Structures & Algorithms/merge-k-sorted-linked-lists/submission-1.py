import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        heap = []
        for li in lists:
            curr = li
            while curr:
                heapq.heappush(heap, NodeWrapper(curr))
                curr = curr.next
        
        if len(heap) == 0:
            return None
        head = heapq.heappop(heap).node
        curr = head
        while heap:
            new = heapq.heappop(heap).node
            curr.next = new
            curr = new
        return head
