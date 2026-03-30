type Solution struct{}

func (s *Solution) Encode(strs []string) string {
	var output string
	for _, str := range strs {
		length := strconv.Itoa(len(str))
		output += length
		output += "|"
		output += str
	}
	fmt.Println(output)
	return output
}

func (s *Solution) Decode(encoded string) []string {
	out := []string{}

	for i := 0; i < len(encoded); {
		j := i
		for encoded[j] != '|' {
			j++
		}
		length, _ := strconv.ParseInt(encoded[i:j],10, 64)
		i = j + 1
		str := encoded[i:i + int(length)]
		out = append(out, str)
		i += int(length)
	}


	return out
}
