import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dist = math.sqrt((x*x)+ (y*y))

    def __lt__(self, other):
        return self.dist < other.dist

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pointlist = [Point(x[0], x[1]) for x in points]
        heapq.heapify(pointlist)
        #print([(x.dist, x.x, x.y) for x in pointlist])
        smallest = heapq.nsmallest(k, pointlist)
        #print([[p.x, p.y, p.dist] for p in smallest])
        return [[p.x, p.y] for p in smallest]