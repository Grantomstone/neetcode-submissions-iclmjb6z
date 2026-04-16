class Solution:
	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
		heap = heapq.merge(nums1, nums2)
		heap = list(heap)
		if len(heap) % 2 == 0:
			mid = len(heap) // 2
			return float(heap[mid - 1] + heap[mid]) / float(2)
		else:
			mid = len(heap) // 2
			return heap[mid]
        