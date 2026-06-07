class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        combined = []
        for i in intervals:
            if len(combined) == 0:
                combined.append(i)
            elif combined[-1][1] > i[0] or combined[-1][1] == i[0]:
                com = combined[-1]
                combined[-1][1] = max(com[1], i[1])
            else:
                combined.append(i)
        return combined