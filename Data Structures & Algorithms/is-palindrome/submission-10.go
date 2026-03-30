func isPalindrome(s string) bool {
	lowered := strings.ToLower(s)
	filtered := []rune{}

	for _, chr := range lowered {
		if (chr >= 'a' && chr <= 'z') || (chr >= '0' && chr <= '9') {
			filtered = append(filtered, chr)
		}
	}

	fmt.Println(filtered)
	length := len(filtered)
	start := 0
	end := length - 1

	for i := 0; i < length / 2; i++ {
		fmt.Println("start:", filtered[start],"\tend:",filtered[end])
		if filtered[start] != filtered[end] {
			return false
		}
		start += 1
		end -= 1
	}
	return true
}
