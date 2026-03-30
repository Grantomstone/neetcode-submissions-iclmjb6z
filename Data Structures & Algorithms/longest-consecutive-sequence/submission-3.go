import ("slices")

func longestConsecutive(nums []int) int {
	if len(nums) == 0 || len(nums) == 1 {
		return len(nums)
	}
	slices.Sort(nums)
	fmt.Println("sorted:",nums)
	maxLength := 1
	currLength := 1
	prevVal := nums[0]

	for i := 1; i < len(nums); i++ {
		fmt.Println("nums[i]:",nums[i], "nums[i-1]:", prevVal)
		if nums[i] - prevVal == 1 {
			currLength++
			fmt.Println("curr:",currLength)
		} else if nums[i] - prevVal == 0 {
			continue
		} else if maxLength < currLength {
			maxLength = currLength
			currLength = 1
			fmt.Println("curr:",currLength,"\tmax:",maxLength)
		} else {
			currLength = 1
			fmt.Println("curr:",currLength)
		}
		prevVal = nums[i]
	}

	if currLength > maxLength {
		return currLength
	} else {
		return maxLength
	}
}
