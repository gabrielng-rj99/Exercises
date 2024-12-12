package main

import (
	"fmt"
	"math"
)

func isPalindrome2(x int) bool {
	if x < 0 {
		return false
	}
	if x < 10 {
		return true
	}

	if x < 100 {
		if x%10 == x/10 {
			return true
		}
		return false
	}

	if x%10 == 0 {
		return false
	}

	houses := 1
	var temp int

	for true {
		temp = x % int(math.Pow10(houses))
		houses += 1
		if temp == x {
			break
		}
	}
	houses -= 1

	inverse := 0
	original := x
	for houses != 0 {
		inverse += int(math.Pow10(houses-1)) * (x % 10)
		x /= 10
		houses -= 1
	}
	return original == inverse
}

// 7424 - 7 - 40 - 200 - 4000
// 5225 - 5 - 20 - 200 - 5000

func main9_2() {
	fmt.Println(isPalindrome2(121))
	fmt.Println(isPalindrome2(123))
	fmt.Println(isPalindrome2(10))
	fmt.Println(isPalindrome2(313))
}
