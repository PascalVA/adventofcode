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

	var currentValue int
	seen := make(map[int]bool)
	numbers := get_input()

	for i := 0; true; i++ {
		if i == len(numbers)-1 {
			i = 0
		}
		currentValue = currentValue + numbers[i]
		if seen[currentValue] {
			break
		} else {
			seen[currentValue] = true
		}
	}

	return currentValue
}

func main() {
	fmt.Println(part1())
	fmt.Println(part2())
}
