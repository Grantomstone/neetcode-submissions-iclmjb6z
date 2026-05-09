"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startTime = [inte.start for inte in intervals]
        endTime = [inte.end for inte in intervals]
        startTime.sort()
        endTime.sort()

        count = 0
        max_count = 0
        s, e = 0,0
        while s < len(startTime) and e < len(endTime):
            if startTime[s] < endTime[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            max_count = max(count, max_count)
        return max_count