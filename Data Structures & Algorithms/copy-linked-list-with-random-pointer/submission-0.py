"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashset = {None: None}
        
        curr = head
        while curr:
            copy = Node(curr.val)
            hashset[curr] = copy
            curr = curr.next
        curr = head
        while curr:
            copy = hashset[curr]
            copy.next = hashset[curr.next]
            copy.random = hashset[curr.random]
            curr = curr.next
        return hashset[head]

        

        