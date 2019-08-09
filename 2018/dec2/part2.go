package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"os"
	"time"
)

func compare_word(a, b []byte) ([]byte, bool) {
	var diffs []int
	for i := 0; i < len(a); i++ {
		if a[i] != b[i] {
			diffs = append(diffs, i)
		}
		if len(diffs) > 1 {
			return []byte{}, false
		}
	}
	return append(a[:diffs[0]], a[diffs[0]+1:]...), true
}

func main() {
	startTime := time.Now()
	defer func() { fmt.Printf("PART 1 took %s\n", time.Since(startTime)) }()

	f, _ := os.Open("input.txt")
	content, _ := ioutil.ReadAll(f)
	s1 := bytes.Split(content[:len(content)-1], []byte("\n"))

	var (
		cw     int
		ok     bool
		result []byte
	)
	for i := 0; i < len(s1); i++ {
		if i != cw {
			result, ok = compare_word(s1[i], s1[cw])
			if ok {
				break
			}
		}
		if cw == len(s1)-1 {
			break
		}
		if i == len(s1)-1 {
			i = 0
			cw = cw + 1
		}
	}
	fmt.Println(string(result))
}
