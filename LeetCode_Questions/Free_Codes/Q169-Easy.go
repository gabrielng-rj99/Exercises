package main

import (
	"fmt"
)

func majorityElement(nums []int) int {
	candidate := 0
	counter := 0

	for _, val := range nums {
		if counter == 0 {
			candidate = val
			counter += 1
		} else if val == candidate {
			counter += 1
		} else {
			counter -= 1
		}
	}
	return candidate
}

func main169() {
	testcases := [][]int{
		{3, 2, 3},
		{2, 2, 1, 1, 1, 2, 2},
		{4, 3, 3, 3, 2, 1, 3, 5, 6, 7, 3, 3, 3},
		{1},
	}

	for _, testcase := range testcases {
		fmt.Println(majorityElement(testcase))
	}
}
