"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        copyMap = {}

        def traverse(node: Node) -> Node:
            if node in copyMap:
                return copyMap[node]

            copy = Node(val=node.val)
            copyMap[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(traverse(neighbor))
            return copy

        return traverse(node)