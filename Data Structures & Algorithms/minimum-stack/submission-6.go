type MinStack struct {
	data []int
	sorted []int
}

func Constructor() MinStack {
	return MinStack {}
}

func (this *MinStack) Push(val int) {
	this.data = append(this.data, val)
	if len(this.sorted) == 0 || val < this.sorted[len(this.sorted) - 1] {
		this.sorted = append(this.sorted, val)
	} else {
		this.sorted = append(this.sorted, this.sorted[len(this.sorted) - 1])
	}
}

func (this *MinStack) Pop() {
	this.data = this.data[:len(this.data) - 1]
	this.sorted = this.sorted[:len(this.sorted) - 1]
}

func (this *MinStack) Top() int {
	return this.data[len(this.data) - 1]
}

func (this *MinStack) GetMin() int {
	return this.sorted[len(this.sorted) - 1]
}
