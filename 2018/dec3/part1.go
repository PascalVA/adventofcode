package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"strconv"
	"time"
)

const size = 1000

var area = make([]int, size*size)

func get_dimensions(b []byte) (int, int, int, int, int) {
	//TODO improve parsing of input string
	idsplit := bytes.Split(b, []byte("@ "))
	spec := bytes.Split(idsplit[1], []byte(": "))
	pos := bytes.Split(spec[0], []byte(","))
	size := bytes.Split(spec[1], []byte("x"))
	id, _ := strconv.Atoi(string(idsplit[0]))
	x, _ := strconv.Atoi(string(pos[0]))
	y, _ := strconv.Atoi(string(pos[1]))
	w, _ := strconv.Atoi(string(size[0]))
	h, _ := strconv.Atoi(string(size[1]))
	return id, x, y, w, h
}

func draw_area(area []int, size int) {
	// TODO: improve this
	y := 0
	for pos := range area {
		if y == size {
			fmt.Printf("\n")
			y = 0
		}
		y++
		fmt.Printf("%d ", area[pos])
	}
	fmt.Printf("\n\n")
}

func count_overlaps(area []int) int {
	var count int
	for pos := range area {
		if area[pos] > 1 {
			count++
		}
	}
	return count
}

func main() {
	startTime := time.Now()
	defer func() { fmt.Printf("PART 1 took %s\n", time.Since(startTime)) }()

	b, _ := ioutil.ReadFile("input.txt")
	lines := bytes.Split(b, []byte("\n"))
	for _, l := range lines[:len(lines)-1] {
		if l[0] == []byte("!")[0] {
			continue
		}
		_, x, y, w, h := get_dimensions(l)

		// make claim
		offset := y*size + x
		max_offset := (y+h-1)*size + x + w
		for i := 0; i <= w; i++ {
			if i == w {
				offset = offset + size
				i = 0
				if offset >= max_offset {
					break
				} else {
					area[offset+i] = area[offset+i] + 1
					continue
				}
			}
			area[offset+i] = area[offset+i] + 1
		}
	}
	//draw_area(area, size)
	fmt.Println(count_overlaps(area))
}