class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.data, num)

    def findMedian(self) -> float:
        if len(self.data) % 2 == 0:
            if len(self.data) == 2:
                return (float(self.data[0]) + float(self.data[1]))/2.0
            else:
                mid = len(self.data) // 2
                small = heapq.nsmallest(mid + 1, self.data)
                return (float(small[-1]) + float(small[-2]))/2.0
        else:
            if len(self.data) == 1:
                return float(self.data[0])
            else:
                mid = len(self.data) // 2
                small = heapq.nsmallest(mid + 1, self.data)
                return float(small[-1])