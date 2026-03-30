func twoSum(numbers []int, target int) []int {
	start := 0
	end := len(numbers) - 1

	for sum := numbers[end] + numbers[start]; sum != target; {
		if sum > target {
			end -= 1
		} else if sum < target {
			start += 1
		} else {
			break
		}
		sum = numbers[end] + numbers[start]
	}
	return []int{start+1, end+1}
}
