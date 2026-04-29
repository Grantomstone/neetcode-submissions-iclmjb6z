import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            a = heapq.heappop_max(stones)
            b = heapq.heappop_max(stones)
            diff = abs(a - b)
            if diff != 0:
                heapq.heappush_max(stones, diff)
        return stones[0] if stones else 0