class Solution:
	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
		#heap = nums1 + nums2
		heap = heapq.merge(nums1, nums2)
		heap = list(heap)
		#for i in nums1:
		#	heapq.heappush(heap, i)
		#for i in nums2:
		#	heapq.heappush(heap, i)
		#print(heap)
		if len(heap) % 2 == 0:
			mid = len(heap) // 2
			#print(f"{heap[mid - 1]} + {heap[mid]} / 2")
			return float(heap[mid - 1] + heap[mid]) / float(2)
		else:
			mid = len(heap) // 2
			return heap[mid]
        