func twoSum(nums []int, target int) []int {
    diffMap := make(map[int]int)
	output := make([]int,2)

	for i, v := range nums {
		diffMap[v] = i
	}

	for j, v := range nums {
		diff := target - v
		val, exists := diffMap[diff]
		if exists && val != j {
			output[0] = j
			output[1] = val
			return output
		}
	}
	return output
}
