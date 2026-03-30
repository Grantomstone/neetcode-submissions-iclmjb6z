func largestRectangleArea(heights []int) int {
	stack := [][2]int{}
	maxArea := 0

	for index, height := range heights {
		startIndex := index
		for len(stack) > 0 && stack[len(stack) - 1][1] > height {
			data := stack[len(stack) - 1]
			i := data[0]
			h := data[1]
			stack = stack[:len(stack) - 1]
			currArea := h * (index - i)
			if currArea > maxArea {
				maxArea = currArea
			}
			startIndex = i
		}
		stack = append(stack, [2]int{startIndex,height})
	} 

	for _, data := range stack {
		index := data[0]
		height := data[1]
		currArea := height * (len(heights) - index)
		if currArea > maxArea {
			maxArea = currArea
		}
	}

	return maxArea

}
