package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
	"time"
)

func get_input() []int {
	var numbers []int

	b, _ := ioutil.ReadFile("input.txt")
	strings := strings.Split(string(b), "\n")
	for i := range(strings) {
		n, _ := strconv.Atoi(strings[i])
		numbers = append(numbers, n)
	}

	return numbers
}

func part1() int {
	startTime := time.Now()
	defer func() { fmt.Printf("PART 1 took %s\n", time.Since(startTime)) }()

	var result int
	numbers := get_input()

	for i := range(numbers) {
		result = result + numbers[i]
	}

	return result
}

func part2() int {
	startTime := time.Now()
	defer func() { fmt.Printf("PART 2 took %s\n", time.Since(startTime)) }()

	var (
		currentValue, hi, lo int
		seen []int
	)
	numbers := get_input()

	for i := 0; true; i++ {
		if i == len(numbers)-1 {
			i = 0
		}
		currentValue = currentValue + numbers[i]

		// if highest number, or lowest number seen
		// it is impossible to be a duplicate
		if currentValue > hi {
			hi = currentValue
		} else if currentValue < lo {
			lo = currentValue
		} else {
			if intInSlice(seen, currentValue) {
				break
			}
		}
		seen = append(seen, currentValue)
	}

	return currentValue
}

func intInSlice(slice []int, n int) bool {
	for i := range(slice) {
		if slice[i] == n {
			return true
		}
	}
        return false
}

func main() {
	fmt.Println(part1())
	fmt.Println(part2())
}
