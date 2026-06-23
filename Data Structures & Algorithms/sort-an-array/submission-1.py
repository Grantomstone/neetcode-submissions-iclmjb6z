class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heap = nums.copy()
        heapq.heapify(heap)
        for i in range(len(nums)):
            nums[i] = heapq.heappop(heap)
        return nums