type MinStack struct {
	data []int
	sorted []int
}

func Constructor() MinStack {
	return MinStack {}
}

func (this *MinStack) Push(val int) {
	fmt.Println("pushed stack\nstack:",this.data, "\nmin:",this.sorted)
	this.data = append(this.data, val)
	if len(this.sorted) == 0 || val < this.sorted[len(this.sorted) - 1] {
		fmt.Println("added val")
		this.sorted = append(this.sorted, val)
	} else {
		fmt.Println("added top of sorted")
		this.sorted = append(this.sorted, this.sorted[len(this.sorted) - 1])
	}
	fmt.Println("pushed stack\nstack:",this.data, "\nmin:",this.sorted)
}

func (this *MinStack) Pop() {
	this.data = this.data[:len(this.data) - 1]
	this.sorted = this.sorted[:len(this.sorted) - 1]
	fmt.Println("popped stack\nstack:",this.data, "\nmin:",this.sorted)
}

func (this *MinStack) Top() int {
	fmt.Println("topped stack\nstack:",this.data, "\nmin:",this.sorted)
	return this.data[len(this.data) - 1]
}

func (this *MinStack) GetMin() int {
	fmt.Println("gave min stack\nstack:",this.data, "\nmin:",this.sorted)
	return this.sorted[len(this.sorted) - 1]
}
