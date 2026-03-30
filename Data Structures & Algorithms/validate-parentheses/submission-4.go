func isValid(s string) bool {
    stack := make([]rune, 0)

	for _, chr := range s {
		if chr == '[' || chr == '{' || chr == '(' {
			stack = append(stack, chr)
		} else if chr == ']' && len(stack) != 0 && stack[len(stack) - 1] == '[' {
			stack = stack[:len(stack) - 1]
		} else if chr == ')' && len(stack) != 0 && stack[len(stack) - 1] == '(' {
			stack = stack[:len(stack) - 1]
		} else if chr == '}' && len(stack) != 0 && stack[len(stack) - 1] == '{' {
			stack = stack[:len(stack) - 1]
		} else {
			stack = append(stack, chr)
		}
	}
	return len(stack) == 0
}
