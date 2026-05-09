class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        chIndex = {}
        for i, ch in enumerate(s):
            chIndex[ch] = i

        output = []
        size = 0
        end = 0
        for i, ch in enumerate(s):
            size += 1
            end = max(end, chIndex[ch])
            if i == end:
                output.append(size)
                size = 0
        return output
