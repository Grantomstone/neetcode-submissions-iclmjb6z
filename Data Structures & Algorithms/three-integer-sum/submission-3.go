import ("slices")

func threeSum(nums []int) [][]int {
	slices.Sort(nums)
	output := [][]int{}
	
	for i, num := range nums[:len(nums) - 2] {
		if num > 0 {
			break
		}
		
		if i > 0 && num == nums[i - 1] {
			continue
		}

		l, r := i + 1, len(nums) - 1
		for sum := num + nums[l] + nums[r]; r > l; sum = num + nums[l] + nums[r] {
			if sum > 0 {
				r -= 1
			} else if sum < 0 {
				l += 1
			} else {
				triplet := []int{num, nums[l], nums[r]}
				output = append(output, triplet)
				l+=1
				r-=1
				for l < r && nums[l] == nums[l - 1] {
					l+= 1
				}
			}
		}
	}
	return output
}