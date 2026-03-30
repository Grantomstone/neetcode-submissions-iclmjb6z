import ("maps")

func isAnagram(s string, t string) bool {
    sMap := make(map[byte]int)
    tMap := make(map[byte]int)

    if len(s) != len(t) {
        return false
    }
    
    for i := 0; i < len(s); i++ {
        sMap[s[i]] += 1
    }

    for i := 0; i < len(t); i++ {
        tMap[t[i]] += 1
    }

    return maps.Equal(sMap, tMap)

}
