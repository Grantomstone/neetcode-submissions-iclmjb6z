class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)

        res = {v:k for k, v in count.items()}
        #print(res)
        return res[max(res.keys())]