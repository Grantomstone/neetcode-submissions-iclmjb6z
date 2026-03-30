class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for num in nums:
            hash[num] = 1 + hash.get(num, 0)
        num_frequency = list(hash.items())#.sort(key=lambda a : a[1])
        num_frequency_2 = sorted(num_frequency, key=lambda a : a[1], reverse=True)
        return [a[0] for a in num_frequency_2[:k]]