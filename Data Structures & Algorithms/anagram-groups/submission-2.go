func groupAnagrams(strs []string) [][]string {

	hashMap := make(map[[26]byte][]string)
	for _, str := range strs {
		var hash [26]byte
		for _, char := range str {
			hash[char - 'a'] += 1
		}
		hashMap[hash] = append(hashMap[hash], str)
	}

	var output [][]string
	for _, group := range hashMap {
		output = append(output, group)
	}
	return output
}
