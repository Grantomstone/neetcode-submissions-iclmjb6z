func search(nums []int, target int) int {
	l, r := 0, len(nums) - 1
    
    for l <= r {
        m := (l + r) / 2
        fmt.Println("l:",l,"\tr:",r,"\tm:",m)
        if target == nums[m] {
            return m
        } else if nums[l] <= nums[m] {
            // l to m sorted
            if nums[l] <= target && target <= nums[m] {
                r = m - 1
            } else {
                l = m + 1
            }
        } else {
            // m to r sorted
            if nums[m] <= target && target <= nums[r] {
                l = m + 1
            } else {
                r = m - 1
            }
        }
    }
    return -1
}
