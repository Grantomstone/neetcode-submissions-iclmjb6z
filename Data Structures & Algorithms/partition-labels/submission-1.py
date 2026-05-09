class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        chIndex = {}
        for i, ch in enumerate(s):
            if ch in chIndex:
                chIndex[ch][1] = i
            else:
                chIndex[ch] = [i,i]
        intervals = list(chIndex.values())
        print(intervals)

        temp = [intervals[0]]
        for start, end in intervals:
            lastend = temp[-1][1]
            if start <= lastend:
                temp[-1][1] = max(lastend, end)
            else:
                temp.append([start, end])
        print(temp)
        return [(b - a + 1) for a,b in temp]
        
