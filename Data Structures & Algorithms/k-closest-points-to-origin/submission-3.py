import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pointlist = [(math.sqrt(x[0]*x[0] + x[1]*x[1]), x[0], x[1]) for x in points]
        heapq.heapify(pointlist)
        output = []
        while len(output) != k:
            _, x, y = heapq.heappop(pointlist)
            output.append([x,y])
        #smallest = heapq.nsmallest(k, pointlist)
        #return [[p[1], p[2]] for p in smallest]
        return output