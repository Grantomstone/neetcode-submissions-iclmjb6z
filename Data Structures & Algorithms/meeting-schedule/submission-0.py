"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key= lambda interval: interval.start)
        for i in range(1, len(intervals)):
            if overlap(intervals[i-1], intervals[i]):
                return False
        return True

def overlap(meeting: Interval, other: Interval) -> bool:
    if meeting.start > other.end or other.start < meeting.end:
        return True
    return False