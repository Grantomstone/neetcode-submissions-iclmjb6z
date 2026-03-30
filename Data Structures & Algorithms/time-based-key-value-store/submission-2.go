type timeMapVal struct {
	Value []string
	Time []int
}

type TimeMap struct {
	maps map[string]*timeMapVal
}

func Constructor() TimeMap {
	return TimeMap {	
		maps: map[string]*timeMapVal{},
	}
}

func (this *TimeMap) Set(key string, value string, timestamp int) {
	val, exists := this.maps[key]
	if !exists {
		this.maps[key] = &timeMapVal{Value: []string{value}, Time: []int{timestamp}}
	} else {
		val.Value = append(val.Value, value)
		val.Time = append(val.Time, timestamp)
	}
}

func (this *TimeMap) Get(key string, timestamp int) string {
	val, exists := this.maps[key]
	if ! exists {
		return ""
	}
	fmt.Println(val.Time)
	l, r := 0, len(val.Time) - 1
	m := 0
	for l <= r {
		m = (l+r)/2
		if timestamp == val.Time[m] {
			return val.Value[m]
		} else if timestamp < val.Time[m] {
			r = m - 1
		} else if val.Time[m] < timestamp {
			l = m + 1
		}
	}

	if timestamp > val.Time[0] {
		for timestamp < val.Time[m] {
			m -= 1
		}
		return val.Value[m]
	} else {
		return ""
	}

	

}
