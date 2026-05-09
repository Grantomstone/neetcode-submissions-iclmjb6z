class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        top, middle, bottom = [],[],[]
        for triple in triplets:
            if triple[0] > target[0] or triple[1] > target[1] or triple[2] > target[2]:
                continue
            top.append(triple[0])
            middle.append(triple[1])
            bottom.append(triple[2])
        if not top:
            return False
        return max(top) == target[0] and max(middle) == target[1] and max(bottom) == target[2]