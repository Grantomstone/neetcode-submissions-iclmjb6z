func min(a,b int) int {
	if a > b {
		return b
	} else {
		return a
	}
}

func maxArea(heights []int) int {
	l := 0
	r := len(heights) - 1
	maxWater := 0

	for 
	currWater := min(heights[l], heights[r]) * (r - l); 
	r > l; 
	currWater = min(heights[l], heights[r]) * (r - l) {
		if currWater > maxWater {
			maxWater = currWater
		}
		if min(heights[l], heights[r]) == heights[l] {
			l++
		} else {
			r--
		}
	}

	return maxWater
}
