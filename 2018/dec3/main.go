package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"strconv"
	"time"
)

const size = 1000

func draw_area(area []int, size int) {
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

func get_dimensions(b []byte) []int {
	//TODO improve parsing of input string
	idsplit := bytes.Split(b, []byte(" @ "))
	spec := bytes.Split(idsplit[1], []byte(": "))
	pos := bytes.Split(spec[0], []byte(","))
	size := bytes.Split(spec[1], []byte("x"))
	id, _ := strconv.Atoi(string(idsplit[0][1:]))
	x, _ := strconv.Atoi(string(pos[0]))
	y, _ := strconv.Atoi(string(pos[1]))
	w, _ := strconv.Atoi(string(size[0]))
	h, _ := strconv.Atoi(string(size[1]))
	return []int{id, x, y, w, h}
}

func get_input() [][]int {
	var claims [][]int

	b, _ := ioutil.ReadFile("input.txt")
	lines := bytes.Split(b, []byte("\n"))
	for _, l := range lines[:len(lines)-1] {
		claims = append(claims, get_dimensions(l))
	}
	return claims
}

// Run a function on each position of a claim within an area
// Returns the sum of all the points in the claim
func process_claim(claim, area []int, f func(pos *int)) int {
	var sum int

	x, y, w, h := claim[1], claim[2], claim[3], claim[4]
	offset := y*size + x               // top-left corner
	max_offset := (y+h-1)*size + x + w // bottom-right corner
	for i := 0; i <= w; i++ {
		if i == w {
			offset = offset + size
			i = 0
			if offset >= max_offset {
				break
			} else {
				f(&area[offset+i])
				sum = sum + area[offset+i]
				continue
			}
		}
		f(&area[offset+i])
		sum = sum + area[offset+i]
	}
	return sum
}

func part1() int {
	startTime := time.Now()
	defer func() { fmt.Printf("PART 1 took %s\n", time.Since(startTime)) }()

	var area = make([]int, size*size)

	claims := get_input()

	// Make claims
	for _, claim := range claims {
		process_claim(claim, area, func(pos *int) {
			*pos = *pos + 1
		})
	}

	var count int
	for pos := range area {
		if area[pos] > 1 {
			count++
		}
	}
	return count
}

func part2() int {
	startTime := time.Now()
	defer func() { fmt.Printf("PART 2 took %s\n", time.Since(startTime)) }()

	var area = make([]int, size*size)

	claims := get_input()

	// Make claims
	for _, claim := range claims {
		process_claim(claim, area, func(pos *int) {
			*pos = *pos + 1
		})
	}

	// Find claim without overlaps
	for _, claim := range claims {
		claim_area := process_claim(claim, area, func(pos *int) { return })
		// if the sum of all points is equal to the area, there can't be any overlaps
		if claim[3]*claim[4] == claim_area {
			return claim[0]
		}
	}

	return 0
}

func main() {
	fmt.Println(part1())
	fmt.Println(part2())
}
