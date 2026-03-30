func search(nums []int, target int) int {
	l,r := 0, len(nums) - 1
	
	for r - l > 1 {
		mid := (l+r)/2
		if nums[mid] > target {
			r = mid
		} else if nums[mid] < target {
			l = mid
		} else if nums[mid] == target {
			return mid
		}
	}
	if nums[l] == target {
		return l
	} else if nums[r] == target {
		return r
	} else {
		return -1
	}
}
