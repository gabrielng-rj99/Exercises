package main

import (
	"fmt"
)

func removeElement(nums []int, val int) int {
	wp := 0
	rp := 0
	counter := 0
	for rp < len(nums) {
		if nums[rp] == val {
			counter += 1
			rp += 1

		} else {
			nums[wp] = nums[rp]
			wp += 1
			rp += 1
		}
	}
	return len(nums) - counter
}

func main29() {
	fmt.Println(removeElement([]int{0, 1, 2, 2, 3, 0, 4, 2}, 2))
	fmt.Println(removeElement([]int{3, 2, 2, 3}, 3))
}
