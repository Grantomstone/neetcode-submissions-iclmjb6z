func evalRPN(tokens []string) int {
	stack := make([]int, 0)

	for _, token := range tokens {
		switch token {
			case "+":
				num1 := stack[len(stack) - 1]
				num2 := stack[len(stack) - 2]
				res := num1 + num2
				stack = stack[:len(stack) - 2]
				stack = append(stack, res)
			case "-":
				num1 := stack[len(stack) - 1]
				num2 := stack[len(stack) - 2]
				res := num2 - num1
				stack = stack[:len(stack) - 2]
				stack = append(stack, res)
			case "*":
			num1 := stack[len(stack) - 1]
				num2 := stack[len(stack) - 2]
				res := num2 * num1
				stack = stack[:len(stack) - 2]
				stack = append(stack, res)
			case "/":
			num1 := stack[len(stack) - 1]
				num2 := stack[len(stack) - 2]
				res := num2 / num1
				stack = stack[:len(stack) - 2]
				stack = append(stack, res)
			default:
				num , _ := strconv.Atoi(token)
				stack = append(stack,num)
		}
	}

	return stack[0]

}
