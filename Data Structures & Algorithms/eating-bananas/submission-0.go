func minEatingSpeed(piles []int, h int) int {
	l,r := 1,0
	for _, val := range piles {
		if val > r {
			r = val
		}
	}
	output := r

	for l <= r {
		mid := (l + r) / 2
		totalTime := 0
		for _, pile := range piles {
			totalTime += int(math.Ceil(float64(pile) / float64(mid)))
		}

		if totalTime <= h {
			output = mid
			r = mid - 1
		} else {
			l = mid + 1
		}
	} 
	return output
}
